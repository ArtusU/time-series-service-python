# Time Series Service
Write a REST API server to track a time-series of data. Implement the endpoints described below with appropriate response statuses. The server should keep the data only in memory, no persistency is necessary.

Good architecture design and clean code are also part of the assessment. We look forward to your solution and also to your suggestions on how to improve the API endpoint architecture.

### Endpoints

- ```POST /datapoints ``` {timestamp;value;device;user} - Add a new datapoint to time series. The set {timestamp, device, user} should be unique (adding the same point should emit an error response and the data should not be changed.) The endpoint should accept JSON object with keys described in brackets (all fields are mandatory)


- ``` DELETE /devices/{device}/datapoints ``` - Delete all device datapoints

- ```DELETE /users/{user}/datapoints ``` - Delete all user datapoints

- ``` GET /statistics/devices/{device}/avg ``` - Return a list of the time-series value averages in 15 minute buckets. The time-range returned should cover the period from first datapoint to current time filtering on datapoints with the provided device key.

- ``` GET /statistics/devices/{device}/moving_avg?window_size={window_size} ``` - Return a list of moving averages of the bucketed 15 minute data provided by the `avg` endpoint. The response should cover the same time-range and also be filtered on the provided device key. The window size (n) should be provided in the query and invalid values should be handled appropriately.

- ``` GET /statistics/users/{user}/avg ``` - Return a list of the time-series value averages in 15 minute buckets. The time-range returned should cover the period from first datapoint to current time filtering on datapoints with the provided user key

- ``` GET /statistics/users/{user}/moving_avg?window_size={window_size} ``` - Return a list of moving averages of the bucketed 15 minute data provided by the `avg` endpoint. The response should cover the same time-range and also be filtered on the provided user key. The window size (n) should be provided in the query and invalid values should be handled appropriately.

#### Moving average formula
The moving average for each bucket can be calculated as follows:
$$ \bar{y_{t}} = { y_{t} + y_{t-1} + ... + y_{t-(n-1)} \over n} $$
Where $n$ is the moving average window size.
