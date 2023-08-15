import uuid
from datetime import datetime

import pandas as pd
from fastapi import HTTPException

from data import datastore
from models import DataPoint


def get_datastore():
    return datastore


def generate_datapoint_key(user_id: uuid.UUID, device_id: uuid.UUID):
    return f"{user_id}_{device_id}_{uuid.uuid4()}"


def add_timestamp_to_datapoint(datapoint: DataPoint, timestamp: datetime):
    return datapoint.model_copy(update={"timestamp": timestamp})


def get_keys_by_device_id(device_id: str):
    return [key for key, val in get_datastore().items() if val.device.id == device_id]


def get_keys_by_user_id(user_id: str):
    return [key for key, val in get_datastore().items() if val.user.id == user_id]


def handle_deletion(keys_to_delete: list):
    for key in keys_to_delete:
        get_datastore().pop(key)


def get_datapoints_by_device_id(device_id: str):
    return [
        (key, val.timestamp, val.value)
        for key, val in get_datastore().items()
        if val.device.id == device_id
    ]


def get_datapoints_by_user_id(user_id: str):
    return [
        (key, val.timestamp, val.value)
        for key, val in get_datastore().items()
        if val.user.id == user_id
    ]


def calculate_avg(datapoints: list) -> list[int]:
    if not datapoints:
        return []

    df = create_dataframe(datapoints)
    time_range = create_time_range(df)

    avg_values = []
    for start_time, end_time in zip(time_range, time_range[1:]):
        subset = get_subset(df, start_time, end_time)
        if not subset.empty:
            avg_value = subset["value"].mean()
            avg_values.append(avg_value)

    return avg_values


def calculate_moving_avg(avg_data: list, window_size: int) -> list[int]:
    if not avg_data:
        return []

    if window_size > len(avg_data):
        raise HTTPException(status_code=400, detail="Invalid window_size")
    moving_avgs = []
    for i in range(len(avg_data) - window_size + 1):
        window = avg_data[i : i + window_size]
        avg_value = sum(entry for entry in window) / window_size
        moving_avgs.append(avg_value)
    return moving_avgs


def create_dataframe(datastore: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(datastore, columns=["key", "timestamp", "value"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def create_time_range(df):
    min_time = df["timestamp"].min()
    current_time = datetime.now()
    return pd.date_range(start=min_time, end=current_time, freq="15T")


def get_subset(df, start_time, end_time):
    return df[(df["timestamp"] >= start_time) & (df["timestamp"] < end_time)]
