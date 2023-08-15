from datetime import datetime

from fastapi import FastAPI, HTTPException, Query

from models import DataPoint
from utils import (
    add_timestamp_to_datapoint,
    calculate_avg,
    calculate_moving_avg,
    generate_datapoint_key,
    get_datapoints_by_device_id,
    get_datapoints_by_user_id,
    get_datastore,
    get_keys_by_device_id,
    get_keys_by_user_id,
    handle_deletion,
)
from validators import validate_id

app = FastAPI(
    title="Time Series Service Task",
    description="REST API server to track a time-series of data.",
)


@app.post("/datapoints")
def create_datapoint(datapoint: DataPoint):
    key = generate_datapoint_key(datapoint.user.id, datapoint.device.id)
    datastore = get_datastore()

    if key in datastore:
        raise HTTPException(status_code=400, detail="Data point already exists")

    current_timestamp = datetime.utcnow()
    datapoint_with_timestamp = add_timestamp_to_datapoint(datapoint, current_timestamp)

    datastore[key] = datapoint_with_timestamp
    return {"message": "Data point added successfully"}


@app.get("/datapoints")
def get_datapoints():
    return get_datastore()


@app.delete("/devices/{device_id}/datapoints")
def delete_device_datapoints(device_id: str):
    device_uuid = validate_id(device_id)

    keys_to_delete = get_keys_by_device_id(device_uuid)

    if not keys_to_delete:
        raise HTTPException(
            status_code=404,
            detail=f"Device '{device_id}' not found or no data points to delete.",
        )

    handle_deletion(keys_to_delete)
    return {"message": "All data points deleted successfully"}


# Delete all user datapoints.
@app.delete("/users/{user_id}/datapoints")
def delete_user_datapoints(user_id: str):
    user_uuid = validate_id(user_id)

    keys_to_delete = get_keys_by_user_id(user_uuid)

    if not keys_to_delete:
        raise HTTPException(
            status_code=404,
            detail=f"User '{user_id}' not found or no data points to delete",
        )

    handle_deletion(keys_to_delete)
    return {"message": f"All data points for user {user_id} deleted successfully"}


# Return a list of the time-series value averages in 15 minute buckets.
@app.get("/statistics/devices/{device_id}/avg")
def get_device_avg(device_id: str):
    device_uuid = validate_id(device_id)
    device_datapoints = get_datapoints_by_device_id(device_uuid)
    return calculate_avg(device_datapoints)


# Return a list of moving averages of the bucketed 15 minute data provided by the avg endpoint.
@app.get("/statistics/devices/{device_id}/moving_avg")
def get_device_moving_avg(device_id: str, window_size: int = Query(..., gt=0)):
    avg_data = get_device_avg(device_id)
    return calculate_moving_avg(avg_data, window_size)


# Return a list of the time-series value averages in 15 minute buckets.
@app.get("/statistics/users/{user_id}/avg")
def get_user_avg(user_id: str):
    user_uuid = validate_id(user_id)
    user_datapoints = get_datapoints_by_user_id(user_uuid)
    return calculate_avg(user_datapoints)


# Return a list of moving averages of the bucketed 15 minute data provided by the avg endpoint.
@app.get("/statistics/users/{user_id}/moving_avg")
def get_user_moving_avg(user_id: str, window_size: int = Query(..., ge=1)):
    avg_data = get_user_avg(user_id)
    return calculate_moving_avg(avg_data, window_size)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
