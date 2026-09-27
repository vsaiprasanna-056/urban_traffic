# Import pandas for data processing
import pandas as pd

# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# Import function to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Import metrics to evaluate the model
from sklearn.metrics import mean_absolute_error, r2_score


# Store the paths of all four NYC taxi files
files = [
    "nyc_yellow/yellow_tripdata_2015-01.csv",
    "nyc_yellow/yellow_tripdata_2016-01.csv",
    "nyc_yellow/yellow_tripdata_2016-02.csv",
    "nyc_yellow/yellow_tripdata_2016-03.csv"
]


# Create an empty list to store only sampled rows
samples = []


# Process each taxi file
for file in files:

    # Read the large CSV file in chunks of 100,000 rows
    for chunk in pd.read_csv(
        file,
        usecols=[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_distance"
        ],
        chunksize=100000
    ):

        # Convert pickup time into datetime format
        chunk["tpep_pickup_datetime"] = pd.to_datetime(
            chunk["tpep_pickup_datetime"],
            errors="coerce"
        )

        # Convert dropoff time into datetime format
        chunk["tpep_dropoff_datetime"] = pd.to_datetime(
            chunk["tpep_dropoff_datetime"],
            errors="coerce"
        )

        # Calculate travel time in minutes
        chunk["travel_time"] = (
            chunk["tpep_dropoff_datetime"]
            - chunk["tpep_pickup_datetime"]
        ).dt.total_seconds() / 60

        # Extract the pickup hour
        chunk["hour"] = chunk["tpep_pickup_datetime"].dt.hour

        # Extract the day of the week
        chunk["day_of_week"] = chunk["tpep_pickup_datetime"].dt.dayofweek

        # Keep only realistic trips
        chunk = chunk[
            (chunk["travel_time"] > 1) &
            (chunk["travel_time"] <= 180) &
            (chunk["trip_distance"] > 0) &
            (chunk["trip_distance"] <= 100)
        ]

        # Take 2% from every chunk to create a representative ML dataset
        sample = chunk.sample(
            frac=0.02,
            random_state=42
        )

        # Add the sample to our list
        samples.append(sample)


# Combine the sampled rows
data = pd.concat(samples, ignore_index=True)


# Create a cyclic representation of the hour
# This represents the circular nature of time
data["hour_sin"] = __import__("numpy").sin(
    2 * __import__("numpy").pi * data["hour"] / 24
)

# Create another cyclic representation of the hour
data["hour_cos"] = __import__("numpy").cos(
    2 * __import__("numpy").pi * data["hour"] / 24
)


# Display the number of rows used for machine learning
print("Rows used for Linear Regression:", len(data))


# Define the input features
X = data[
    [
        "trip_distance",
        "hour_sin",
        "hour_cos",
        "day_of_week"
    ]
]


# Define the target
# We want to predict travel time
y = data["travel_time"]


# Split the data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create the Linear Regression model
model = LinearRegression()


# Train the model
model.fit(X_train, y_train)


# Predict travel time for the test data
y_pred = model.predict(X_test)


# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)


# Calculate R2 score
r2 = r2_score(y_test, y_pred)


# Display the model results
print("\nLinear Regression Results")
print("-------------------------")
print("Mean Absolute Error:", round(mae, 2), "minutes")
print("R2 Score:", round(r2, 4))


# Create example trips for prediction
example = pd.DataFrame({
    "trip_distance": [2, 5, 10],
    "hour": [8, 12, 18],
    "day_of_week": [0, 2, 4]
})


# Calculate hour sine value for the examples
example["hour_sin"] = __import__("numpy").sin(
    2 * __import__("numpy").pi * example["hour"] / 24
)

# Calculate hour cosine value for the examples
example["hour_cos"] = __import__("numpy").cos(
    2 * __import__("numpy").pi * example["hour"] / 24
)


# Select the same features used during training
example_features = example[
    [
        "trip_distance",
        "hour_sin",
        "hour_cos",
        "day_of_week"
    ]
]


# Predict travel time for the example trips
example["predicted_travel_time"] = model.predict(
    example_features
)


# Display the example predictions
print("\nExample Travel-Time Predictions:")
print(
    example[
        [
            "trip_distance",
            "hour",
            "day_of_week",
            "predicted_travel_time"
        ]
    ]
)


