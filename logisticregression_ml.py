# Import pandas for data processing
import pandas as pd

# Import Logistic Regression
from sklearn.linear_model import LogisticRegression

# Import train-test split
from sklearn.model_selection import train_test_split

# Import evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Import os to create the output folder if needed
import os


# --------------------------------------------------
# 1. File locations
# --------------------------------------------------

# Store the paths of your 4 NYC taxi files
files = [
    "nyc_yellow/yellow_tripdata_2015-01.csv",
    "nyc_yellow/yellow_tripdata_2016-01.csv",
    "nyc_yellow/yellow_tripdata_2016-02.csv",
    "nyc_yellow/yellow_tripdata_2016-03.csv"
]


# --------------------------------------------------
# 2. Create hourly traffic intervals
# --------------------------------------------------

# Create an empty list to store hourly results
hourly_data = []


# Process each large CSV file one at a time
for file in files:

    print("\nProcessing:", file)

    # Read only the pickup datetime column
    # This saves memory
    for chunk in pd.read_csv(
        file,
        usecols=["tpep_pickup_datetime"],
        chunksize=200000
    ):

        # Convert pickup time into datetime format
        chunk["pickup_time"] = pd.to_datetime(
            chunk["tpep_pickup_datetime"],
            errors="coerce"
        )

        # Remove invalid datetime values
        chunk = chunk.dropna(
            subset=["pickup_time"]
        )

        # Extract the date
        chunk["date"] = chunk["pickup_time"].dt.date

        # Extract the hour
        chunk["hour"] = chunk["pickup_time"].dt.hour

        # Extract the day of week
        # Monday = 0 and Sunday = 6
        chunk["day_of_week"] = (
            chunk["pickup_time"].dt.dayofweek
        )

        # Count trips for each date and hour
        grouped = (
            chunk
            .groupby(
                ["date", "hour", "day_of_week"]
            )
            .size()
            .reset_index(
                name="trip_count"
            )
        )

        # Store the result
        hourly_data.append(grouped)


# --------------------------------------------------
# 3. Combine all hourly results
# --------------------------------------------------

# Combine results from all chunks
df = pd.concat(
    hourly_data,
    ignore_index=True
)


# Group again because the same date/hour
# may have appeared in different chunks
df = (
    df
    .groupby(
        ["date", "hour", "day_of_week"],
        as_index=False
    )["trip_count"]
    .sum()
)


# Display number of observations
print("\nTotal hourly intervals:", len(df))


# --------------------------------------------------
# 4. Create high-congestion target
# --------------------------------------------------

# Calculate the median trip count
# This becomes our congestion threshold
trip_median = df["trip_count"].median()

# Create target variable
# 1 = High congestion
# 0 = Normal congestion
df["high_congestion"] = (
    df["trip_count"] >= trip_median
).astype(int)


# Display threshold
print(
    "\nTrip count threshold:",
    trip_median
)


# --------------------------------------------------
# 5. Create useful features
# --------------------------------------------------

# Create peak-hour indicator
# These are common morning and evening peak periods
df["peak_hour"] = (
    df["hour"].isin(
        [7, 8, 9, 17, 18, 19]
    )
).astype(int)


# Create weekend indicator
# Saturday = 5
# Sunday = 6
df["weekend"] = (
    df["day_of_week"] >= 5
).astype(int)


# --------------------------------------------------
# 6. Select features
# --------------------------------------------------

# These features are used to predict congestion
features = [
    "hour",
    "day_of_week",
    "peak_hour",
    "weekend"
]


# Create input data
X = df[features]

# Create target data
y = df["high_congestion"]


# --------------------------------------------------
# 7. Split data into training and testing
# --------------------------------------------------

# Use 80% for training
# Use 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Display dataset sizes
print("\nTraining observations:", len(X_train))
print("Testing observations:", len(X_test))


# --------------------------------------------------
# 8. Create Logistic Regression model
# --------------------------------------------------

# Create the Logistic Regression model
model = LogisticRegression(
    max_iter=1000
)


# Train the model
model.fit(
    X_train,
    y_train
)


# --------------------------------------------------
# 9. Make predictions
# --------------------------------------------------

# Predict congestion class
y_pred = model.predict(
    X_test
)


# --------------------------------------------------
# 10. Evaluate the model
# --------------------------------------------------

# Calculate accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)


# Display accuracy
print(
    "\nModel Accuracy:",
    round(accuracy, 4)
)


# --------------------------------------------------
# 11. Confusion Matrix
# --------------------------------------------------

# Calculate confusion matrix
cm = confusion_matrix(
    y_test,
    y_pred
)


# Display confusion matrix
print("\nConfusion Matrix:")
print(cm)


# --------------------------------------------------
# 12. Classification Report
# --------------------------------------------------

# Display precision, recall and F1-score
print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# --------------------------------------------------
# 13. Predict congestion probability
# --------------------------------------------------

# Create all 24 hours
future_hours = pd.DataFrame({
    "hour": range(24)
})


# Use Monday as the reference day
# for the hourly prediction table
future_hours["day_of_week"] = 0


# Create peak-hour indicator
future_hours["peak_hour"] = (
    future_hours["hour"].isin(
        [7, 8, 9, 17, 18, 19]
    )
).astype(int)


# Monday is a weekday
future_hours["weekend"] = 0


# Predict congestion
future_hours[
    "predicted_high_congestion"
] = model.predict(
    future_hours[features]
)


# Calculate probability of high congestion
future_hours[
    "congestion_probability"
] = model.predict_proba(
    future_hours[features]
)[:, 1]


# --------------------------------------------------
# 14. Display hourly predictions
# --------------------------------------------------

print(
    "\nPredicted Congestion by Hour:"
)

print(
    future_hours.to_string(
        index=False
    )
)


# --------------------------------------------------
# 15. Save results
# --------------------------------------------------

# Make sure results folder exists
os.makedirs(
    "results_csv",
    exist_ok=True
)


# Save hourly congestion predictions
future_hours.to_csv(
    "results_csv/congestion_predictions.csv",
    index=False
)


# Save the classification dataset
df.to_csv(
    "results_csv/congestion_classification_data.csv",
    index=False
)


# --------------------------------------------------
# 16. Completion message
# --------------------------------------------------

print(
    "\nCongestion Logistic Regression "
    "analysis completed successfully!"
)