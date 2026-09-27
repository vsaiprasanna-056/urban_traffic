# Import pandas for working with data
import pandas as pd

# Import numpy for mathematical calculations
import numpy as np

# Import Linear Regression
from sklearn.linear_model import LinearRegression

# Import Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor

# Import XGBoost Regressor
from xgboost import XGBRegressor

# Import functions for splitting data and calculating metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


# List all 4 NYC taxi files
files = [
    "nyc_yellow/yellow_tripdata_2015-01.csv",
    "nyc_yellow/yellow_tripdata_2016-01.csv",
    "nyc_yellow/yellow_tripdata_2016-02.csv",
    "nyc_yellow/yellow_tripdata_2016-03.csv"
]


# Create an empty list to store sampled data
all_data = []


# Process each taxi file one by one
for file in files:

    # Read the CSV file in smaller chunks to save memory
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

        # Get pickup hour
        chunk["hour"] = chunk["tpep_pickup_datetime"].dt.hour

        # Get day of week
        # Monday = 0 and Sunday = 6
        chunk["day_of_week"] = chunk["tpep_pickup_datetime"].dt.dayofweek

        # Remove invalid travel times and distances
        chunk = chunk[
            (chunk["travel_time"] > 1) &
            (chunk["travel_time"] <= 180) &
            (chunk["trip_distance"] > 0) &
            (chunk["trip_distance"] <= 100)
        ]

        # Take 2% of each chunk
        sample = chunk.sample(frac=0.02, random_state=42)

        # Add the sample to our list
        all_data.append(sample)


# Combine all sampled data
data = pd.concat(all_data, ignore_index=True)


# Create sine representation of hour
data["hour_sin"] = np.sin(2 * np.pi * data["hour"] / 24)

# Create cosine representation of hour
data["hour_cos"] = np.cos(2 * np.pi * data["hour"] / 24)


# Select input features
X = data[
    [
        "trip_distance",
        "hour_sin",
        "hour_cos",
        "day_of_week"
    ]
]

# Select target value
# We want to predict travel time
y = data["travel_time"]


# Split data into training and testing sets
# 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# -------------------------------
# 1. LINEAR REGRESSION
# -------------------------------

# Create Linear Regression model
linear_model = LinearRegression()

# Train the model
linear_model.fit(X_train, y_train)

# Predict travel time
linear_prediction = linear_model.predict(X_test)

# Calculate MAE
linear_mae = mean_absolute_error(
    y_test,
    linear_prediction
)

# Calculate R2 score
linear_r2 = r2_score(
    y_test,
    linear_prediction
)


# -------------------------------
# 2. RANDOM FOREST
# -------------------------------

# Create Random Forest Regressor
random_forest = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

# Train Random Forest
random_forest.fit(X_train, y_train)

# Predict travel time
rf_prediction = random_forest.predict(X_test)

# Calculate MAE
rf_mae = mean_absolute_error(
    y_test,
    rf_prediction
)

# Calculate R2 score
rf_r2 = r2_score(
    y_test,
    rf_prediction
)


# -------------------------------
# 3. XGBOOST
# -------------------------------

# Create XGBoost Regressor
xgb_model = XGBRegressor(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1,
    objective="reg:squarederror"
)

# Train XGBoost
xgb_model.fit(X_train, y_train)

# Predict travel time
xgb_prediction = xgb_model.predict(X_test)

# Calculate MAE
xgb_mae = mean_absolute_error(
    y_test,
    xgb_prediction
)

# Calculate R2 score
xgb_r2 = r2_score(
    y_test,
    xgb_prediction
)


# -------------------------------
# DISPLAY RESULTS
# -------------------------------

# Create a table containing all model results
results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest",
        "XGBoost"
    ],
    "MAE": [
        linear_mae,
        rf_mae,
        xgb_mae
    ],
    "R2": [
        linear_r2,
        rf_r2,
        xgb_r2
    ]
})


# Display results
print("\nModel Comparison:")
print(results)


# Find the model with the lowest MAE
best_model = results.loc[
    results["MAE"].idxmin(),
    "Model"
]


# Print the best model
print("\nBest Model based on MAE:", best_model)








# | Model                   | What it predicts                      | Metric   |  Your result | Meaning                         |
# | ----------------------- | ------------------------------------- | -------- | -----------: | ------------------------------- |
# | **Linear Regression**   | Travel time                           | MAE      | **4.10 min** | Average error is 4.1 min        |
# |                         |                                       | R²       |    **0.639** | Explains about 64% of variation |
# | **Random Forest**       | Travel time                           | MAE      | **3.15 min** | Better than Linear              |
# |                         |                                       | R²       |    **0.752** | Explains about 75%              |
# | **XGBoost** 🏆          | Travel time                           | MAE      | **3.11 min** | Best error                      |
# |                         |                                       | R²       |    **0.758** | Best overall                    |
# | **Logistic Regression** | High congestion / Not high congestion | Accuracy |     **100%** | Correctly classified test data  |
