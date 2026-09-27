# Import pandas library for working with data
import pandas as pd


# Read only 1,000 rows from the Taxi CSV file
# We use 1,000 rows now because the complete dataset is very large
taxi_sample = pd.read_csv(
    "nyc_yellow/yellow_tripdata_2015-01.csv",
    nrows=1000
)


# Display the number of rows and columns
# print(taxi_sample.shape)


# Display the names of all columns
# print(taxi_sample.columns.tolist())


# Check how many missing values are present in each column
# print(taxi_sample.isnull().sum())


# Check how many completely duplicate rows are present
# print("Duplicate rows:", taxi_sample.duplicated().sum())


# Check how many trips have zero distance
# print("Zero distance:", (taxi_sample["trip_distance"] == 0).sum())


# Check how many trips have negative distance
# print("Negative distance:", (taxi_sample["trip_distance"] < 0).sum())


# Check how many trips have zero fare
# print("Zero fare:", (taxi_sample["fare_amount"] == 0).sum())


# Check how many trips have negative fare
# print("Negative fare:", (taxi_sample["fare_amount"] < 0).sum())


# Check how many trips have zero passengers
# print("Zero passengers:", (taxi_sample["passenger_count"] == 0).sum())


# Check how many trips have negative passengers
# print("Negative passengers:", (taxi_sample["passenger_count"] < 0).sum())


# Convert the pickup date/time column into Pandas date/time format
taxi_sample["pickup_time"] = pd.to_datetime(
    taxi_sample["tpep_pickup_datetime"]
)


# Convert the drop-off date/time column into Pandas date/time format
taxi_sample["dropoff_time"] = pd.to_datetime(
    taxi_sample["tpep_dropoff_datetime"]
)


# Calculate the trip duration in minutes
# Drop-off time - pickup time gives the travel time
# total_seconds() converts the time difference into seconds
# Dividing by 60 converts seconds into minutes
taxi_sample["trip_duration"] = (
    taxi_sample["dropoff_time"] - taxi_sample["pickup_time"]
).dt.total_seconds() / 60


# Display summary statistics of trip duration
# print(taxi_sample["trip_duration"].describe())

# Count trips where the calculated duration is exactly zero minutes
# print("Zero duration:", (taxi_sample["trip_duration"] == 0).sum())

# Count trips where the calculated duration is negative
# print("Negative duration:", (taxi_sample["trip_duration"] < 0).sum())

# Count trips where the duration is more than 24 hours
# print("Duration above 24 hours:", (taxi_sample["trip_duration"] > 1440).sum())

# Select the trip where the calculated duration is zero minutes
zero_duration_trips = taxi_sample[taxi_sample["trip_duration"] == 0]

# Display the pickup time, drop-off time, distance, and fare of that trip
# print(
#     zero_duration_trips[
#         [
#             "pickup_time",
#             "dropoff_time",
#             "trip_distance",
#             "fare_amount"
#         ]
#     ]
# )


# Find the maximum trip distance in our sample
# print("Maximum distance:", taxi_sample["trip_distance"].max())

# # Find the minimum trip distance in our sample
# print("Minimum distance:", taxi_sample["trip_distance"].min())

# # Show summary statistics for trip distance
# print(taxi_sample["trip_distance"].describe())


# Find the maximum fare amount in our sample
# print("Maximum fare:", taxi_sample["fare_amount"].max())

# # Find the minimum fare amount in our sample
# print("Minimum fare:", taxi_sample["fare_amount"].min())

# # Show summary statistics for fare amount
# print(taxi_sample["fare_amount"].describe())

# # Count how many trips have a zero fare
# print("Zero fare:", (taxi_sample["fare_amount"] == 0).sum())

# # Count how many trips have a negative fare
# print("Negative fare:", (taxi_sample["fare_amount"] < 0).sum())

# Find the maximum number of passengers in a trip
# print("Maximum passengers:", taxi_sample["passenger_count"].max())

# # Find the minimum number of passengers in a trip
# print("Minimum passengers:", taxi_sample["passenger_count"].min())

# # Show summary statistics for passenger count
# print(taxi_sample["passenger_count"].describe())

# # Count trips where the passenger count is zero
# print("Zero passengers:", (taxi_sample["passenger_count"] == 0).sum())

# # Count trips where the passenger count is negative
# print("Negative passengers:", (taxi_sample["passenger_count"] < 0).sum())


# Display the earliest pickup time in our sample
# print("Earliest pickup:", taxi_sample["pickup_time"].min())

# # Display the latest pickup time in our sample
# print("Latest pickup:", taxi_sample["pickup_time"].max())

# # Extract the hour from the pickup time
taxi_sample["hour"] = taxi_sample["pickup_time"].dt.hour

# # Display the first 20 pickup hours
# print("Pickup hours:")
# print(taxi_sample["hour"].head(20))

# # Count how many trips happened during each hour
# print("Trips by hour:")
# print(taxi_sample["hour"].value_counts().sort_index())


# Extract the day of the week from the pickup time
taxi_sample["day_of_week"] = taxi_sample["pickup_time"].dt.day_name()

# Check the first 10 day names
# print("Day of week:")
# print(taxi_sample["day_of_week"].head(10))

# Create a column that identifies whether the trip happened on a weekday or weekend
taxi_sample["weekday_weekend"] = taxi_sample["pickup_time"].dt.dayofweek.apply(
    lambda x: "Weekend" if x >= 5 else "Weekday"
)

# Display the first 10 weekday/weekend values
# print("Weekday or Weekend:")
# print(taxi_sample["weekday_weekend"].head(10))

# # Count the number of trips for each day of the week
# print("Trips by day:")
# print(taxi_sample["day_of_week"].value_counts())

# # Count the number of weekday and weekend trips
# print("Weekday vs Weekend:")
# print(taxi_sample["weekday_weekend"].value_counts())


# Extract the month number from the pickup time
taxi_sample["month"] = taxi_sample["pickup_time"].dt.month

# Display the first 10 month values
# print("Month:")
# print(taxi_sample["month"].head(10))

# # Count how many trips occurred in each month
# print("Trips by month:")
# print(taxi_sample["month"].value_counts().sort_index())



# Read the complete January 2015 taxi dataset
taxi = pd.read_csv("nyc_yellow/yellow_tripdata_2015-01.csv")

# Display the number of rows and columns in the full dataset
# print("Original shape:", taxi.shape)

# # Display the first 5 rows of the dataset
# print(taxi.head())

# Check how many missing values are present in each column
# print("Missing values:")
# print(taxi.isnull().sum())

# # Count completely duplicate rows in the full dataset
# print("Duplicate rows:", taxi.duplicated().sum())


# Count trips where the distance is zero
# print("Zero distance:", (taxi["trip_distance"] == 0).sum())

# # Count trips where the distance is negative
# print("Negative distance:", (taxi["trip_distance"] < 0).sum())

# # Count trips where the fare is zero
# print("Zero fare:", (taxi["fare_amount"] == 0).sum())

# # Count trips where the fare is negative
# print("Negative fare:", (taxi["fare_amount"] < 0).sum())

# # Count trips where the passenger count is zero
# print("Zero passengers:", (taxi["passenger_count"] == 0).sum())

# # Count trips where the passenger count is negative
# print("Negative passengers:", (taxi["passenger_count"] < 0).sum())


# Convert the pickup date/time column into Pandas datetime format
taxi["pickup_time"] = pd.to_datetime(taxi["tpep_pickup_datetime"])

# Convert the drop-off date/time column into Pandas datetime format
taxi["dropoff_time"] = pd.to_datetime(taxi["tpep_dropoff_datetime"])

# Calculate the trip duration in minutes
taxi["trip_duration"] = (
    taxi["dropoff_time"] - taxi["pickup_time"]
).dt.total_seconds() / 60

# Count trips with zero duration
# print("Zero duration:", (taxi["trip_duration"] == 0).sum())

# # Count trips with negative duration
# print("Negative duration:", (taxi["trip_duration"] < 0).sum())

# # Count trips longer than 24 hours
# print("Duration above 24 hours:", (taxi["trip_duration"] > 1440).sum())

# # Display summary statistics for trip duration
# print(taxi["trip_duration"].describe())


# Count trips where the drop-off time is earlier than the pickup time
# print(
#     "Drop-off before pickup:",
#     (taxi["dropoff_time"] < taxi["pickup_time"]).sum()
# )

# # Find the earliest pickup time in the full dataset
# print("Earliest pickup:", taxi["pickup_time"].min())

# # Find the latest pickup time in the full dataset
# print("Latest pickup:", taxi["pickup_time"].max())

# Remove completely duplicate rows from the dataset
taxi = taxi.drop_duplicates()

# Remove rows where improvement_surcharge is missing
taxi = taxi.dropna(subset=["improvement_surcharge"])

# Keep only trips with a positive distance
taxi = taxi[taxi["trip_distance"] > 0]

# Keep only trips with a positive fare
taxi = taxi[taxi["fare_amount"] > 0]

# Keep only trips with at least one passenger
taxi = taxi[taxi["passenger_count"] > 0]

# Keep only trips with a positive travel duration
taxi = taxi[taxi["trip_duration"] > 0]

# Remove trips that lasted more than 24 hours
taxi = taxi[taxi["trip_duration"] <= 1440]

# Display the number of rows and columns after cleaning
# print("Cleaned shape:", taxi.shape)

# # Display the number of rows removed during cleaning
# print("Rows removed:", 12748986 - len(taxi))

# Check whether any duplicate rows remain
# print("Remaining duplicates:", taxi.duplicated().sum())

# # Check whether any trips still have zero or negative distance
# print("Invalid distance:", (taxi["trip_distance"] <= 0).sum())

# # Check whether any trips still have zero or negative fare
# print("Invalid fare:", (taxi["fare_amount"] <= 0).sum())

# # Check whether any trips still have zero or negative passengers
# print("Invalid passengers:", (taxi["passenger_count"] <= 0).sum())

# # Check whether any trips still have zero or negative duration
# print("Invalid duration:", (taxi["trip_duration"] <= 0).sum())

# # Check whether any trips still have a duration above 24 hours
# print("Duration above 24 hours:", (taxi["trip_duration"] > 1440).sum())

# # Check whether improvement_surcharge still has missing values
# print("Missing surcharge:", taxi["improvement_surcharge"].isnull().sum())


# Extract the hour from the pickup time
taxi["hour"] = taxi["pickup_time"].dt.hour

# Extract the day of the week as a number
# Monday = 0 and Sunday = 6
taxi["day_of_week_num"] = taxi["pickup_time"].dt.dayofweek

# Convert the day number into the actual day name
taxi["day_of_week"] = taxi["pickup_time"].dt.day_name()

# Identify whether each trip happened on a weekday or weekend
taxi["weekday_weekend"] = taxi["day_of_week_num"].apply(
    lambda x: "Weekend" if x >= 5 else "Weekday"
)

# Extract the month number from the pickup time
taxi["month"] = taxi["pickup_time"].dt.month

# Display the first 5 rows of the new analytical columns
# print(
#     taxi[
#         [
#             "pickup_time",
#             "trip_duration",
#             "hour",
#             "day_of_week",
#             "weekday_weekend",
#             "month"
#         ]
#     ].head()
# )



# Count the number of taxi trips for each hour
trips_by_hour = taxi["hour"].value_counts().sort_index()

# Display the number of trips for every hour
# print("Trips by hour:")
# print(trips_by_hour)

# Find the hour with the highest number of trips
peak_hour = trips_by_hour.idxmax()

# Find the number of trips during the peak hour
peak_trip_count = trips_by_hour.max()

# Display the peak hour and its trip count
# print("Peak hour:", peak_hour)
# print("Trips during peak hour:", peak_trip_count)

# Count the number of trips for weekdays and weekends
trips_by_day_type = taxi["weekday_weekend"].value_counts()

# Display the weekday and weekend trip counts
# print("Weekday vs Weekend trips:")
# print(trips_by_day_type)

# Calculate the percentage of trips occurring on weekdays
weekday_percentage = (
    (trips_by_day_type["Weekday"] / len(taxi)) * 100
)

# Calculate the percentage of trips occurring on weekends
weekend_percentage = (
    (trips_by_day_type["Weekend"] / len(taxi)) * 100
)

# Display the weekday percentage
# print("Weekday percentage:", weekday_percentage)

# # Display the weekend percentage
# print("Weekend percentage:", weekend_percentage)

# Count the number of taxi trips for each day of the week
trips_by_day = taxi["day_of_week"].value_counts()

# Arrange the days in normal weekly order
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Reorder the results according to the normal week order
trips_by_day = trips_by_day.reindex(day_order)

# Display the number of trips for each day
# print("Trips by day of week:")
# print(trips_by_day)

# Find the day with the highest number of trips
busiest_day = trips_by_day.idxmax()

# Find the number of trips on the busiest day
busiest_day_count = trips_by_day.max()

# Display the busiest day
# print("Busiest day:", busiest_day)

# # Display the number of trips on the busiest day
# print("Trips on busiest day:", busiest_day_count)

# Count the number of taxi trips for each day of the week
trips_by_day = taxi["day_of_week"].value_counts()

# Arrange the days in normal weekly order
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Reorder the results according to the normal week order
trips_by_day = trips_by_day.reindex(day_order)

# Display the number of trips for each day
# print("Trips by day of week:")
# print(trips_by_day)

# Find the day with the highest number of trips
busiest_day = trips_by_day.idxmax()

# Find the number of trips on the busiest day
busiest_day_count = trips_by_day.max()

# Display the busiest day
# print("Busiest day:", busiest_day)

# # Display the number of trips on the busiest day
# print("Trips on busiest day:", busiest_day_count)

# Calculate the average trip duration for each hour
average_duration_by_hour = taxi.groupby("hour")["trip_duration"].mean()

# Display the average trip duration for each hour
# print("Average trip duration by hour:")
# print(average_duration_by_hour)

# Find the hour with the highest average trip duration
slowest_hour = average_duration_by_hour.idxmax()

# Find the highest average trip duration
slowest_duration = average_duration_by_hour.max()

# Display the hour with the highest average duration
# print("Hour with highest average trip duration:", slowest_hour)

# # Display the highest average trip duration in minutes
# print("Highest average trip duration:", slowest_duration, "minutes")

# Calculate the average trip duration for each day of the week
average_duration_by_day = taxi.groupby("day_of_week")["trip_duration"].mean()

# Arrange the days in normal weekly order
average_duration_by_day = average_duration_by_day.reindex(day_order)

# Display the average trip duration for each day
# print("Average trip duration by day:")
# print(average_duration_by_day)

# Find the day with the highest average trip duration
slowest_day = average_duration_by_day.idxmax()

# Find the highest average trip duration
slowest_day_duration = average_duration_by_day.max()

# Display the day with the highest average trip duration
# print("Day with highest average trip duration:", slowest_day)

# # Display the highest average trip duration
# print("Highest average trip duration:", slowest_day_duration, "minutes")

# Calculate the overall average trip duration
overall_average_duration = taxi["trip_duration"].mean()

# Display the overall average trip duration
# print("Overall average trip duration:", overall_average_duration, "minutes")

# Create a congestion category based on the average trip duration
taxi["congestion_level"] = taxi["trip_duration"].apply(
    lambda x: "High Congestion" if x > overall_average_duration else "Normal"
)

# Count how many trips belong to each congestion category
congestion_counts = taxi["congestion_level"].value_counts()

# Display the number of trips in each congestion category
# print("Congestion level counts:")
# print(congestion_counts)

# Calculate the percentage of trips in each congestion category
congestion_percentage = (
    taxi["congestion_level"].value_counts(normalize=True) * 100
)

# Display the congestion percentages
# print("Congestion level percentage:")
# print(congestion_percentage)

# Delete the large January 2015 dataframe from memory
del taxi

# Import garbage collection for freeing unused memory
import gc

# Ask Python to clean unused memory
gc.collect()


# Store the paths of all four NYC Taxi datasets
taxi_files = [
    "nyc_yellow/yellow_tripdata_2015-01.csv",  # January 2015
    "nyc_yellow/yellow_tripdata_2016-01.csv",  # January 2016
    "nyc_yellow/yellow_tripdata_2016-02.csv",  # February 2016
    "nyc_yellow/yellow_tripdata_2016-03.csv"   # March 2016
]

# Display a heading so we know this new process has started
# print("Taxi files selected for processing:")

# Go through each file in the list
# for file in taxi_files:

#     # Display the current file name
#     print(file)

# Process each taxi file one at a time
# for file in taxi_files:

#     # Display which file Python is currently processing
#     print("\nProcessing:", file)

#     # Read the current CSV file in smaller chunks of 500,000 rows
#     for chunk in pd.read_csv(file, chunksize=500000):

#         # Convert pickup time into datetime format
#         chunk["pickup_time"] = pd.to_datetime(chunk["tpep_pickup_datetime"])

#         # Convert drop-off time into datetime format
#         chunk["dropoff_time"] = pd.to_datetime(chunk["tpep_dropoff_datetime"])

#         # Calculate trip duration in minutes
#         chunk["trip_duration"] = (
#             chunk["dropoff_time"] - chunk["pickup_time"]
#         ).dt.total_seconds() / 60

#         # Keep only valid trips
#         chunk = chunk[
#             (chunk["trip_distance"] > 0) &
#             (chunk["fare_amount"] > 0) &
#             (chunk["passenger_count"] > 0) &
#             (chunk["trip_duration"] > 0) &
#             (chunk["trip_duration"] <= 1440)
#         ]

#         # Display how many valid rows are present in this chunk
#         print("Valid rows in this chunk:", len(chunk))






# Create an empty list to store summary information for each taxi file
file_results = []

# Create an empty dictionary to store hourly trip information
hour_results = {}

# Create an empty dictionary to store day-of-week information
day_results = {}

# Create an empty dictionary to store weekday and weekend information
day_type_results = {}


# Process each taxi dataset one at a time
for file in taxi_files:

    # Display which file is currently being processed
    print("\nProcessing:", file)

    # Store the number of valid trips for this file
    total_trips = 0

    # Store the total trip duration for calculating the average later
    total_duration = 0

    # Read the CSV file in chunks of 500,000 rows
    for chunk in pd.read_csv(
        file,
        chunksize=500000,
        usecols=[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "passenger_count",
            "trip_distance",
            "fare_amount",
            "improvement_surcharge"
        ]
    ):

        # Convert pickup time into datetime format
        chunk["pickup_time"] = pd.to_datetime(
            chunk["tpep_pickup_datetime"],
            errors="coerce"
        )

        # Convert drop-off time into datetime format
        chunk["dropoff_time"] = pd.to_datetime(
            chunk["tpep_dropoff_datetime"],
            errors="coerce"
        )

        # Calculate trip duration in minutes
        chunk["trip_duration"] = (
            chunk["dropoff_time"] - chunk["pickup_time"]
        ).dt.total_seconds() / 60

        # Remove duplicate rows inside the current chunk
        chunk = chunk.drop_duplicates()

        # Keep only valid taxi trips
        chunk = chunk[
            chunk["pickup_time"].notna() &
            chunk["dropoff_time"].notna() &
            (chunk["trip_distance"] > 0) &
            (chunk["fare_amount"] > 0) &
            (chunk["passenger_count"] > 0) &
            (chunk["trip_duration"] > 0) &
            (chunk["trip_duration"] <= 1440)
        ]

        # Create the hour column from pickup time
        chunk["hour"] = chunk["pickup_time"].dt.hour

        # Create the day-of-week column
        chunk["day_of_week"] = chunk["pickup_time"].dt.day_name()

        # Create weekday/weekend classification
        chunk["day_type"] = chunk["pickup_time"].dt.dayofweek.map(
            lambda x: "Weekend" if x >= 5 else "Weekday"
        )

        # Add the number of valid trips in this chunk to the file total
        total_trips += len(chunk)

        # Add the duration of all valid trips to the file total
        total_duration += chunk["trip_duration"].sum()

        # Count trips for each hour
        hourly_counts = chunk["hour"].value_counts()

        # Add hourly counts to the overall hourly dictionary
        for hour, count in hourly_counts.items():

            # If the hour does not exist yet, create it
            if hour not in hour_results:
                hour_results[hour] = 0

            # Add the current chunk's trips to that hour
            hour_results[hour] += count

        # Count trips for each day
        daily_counts = chunk["day_of_week"].value_counts()

        # Add daily counts to the overall day dictionary
        for day, count in daily_counts.items():

            # If the day does not exist yet, create it
            if day not in day_results:
                day_results[day] = 0

            # Add the current chunk's trips to that day
            day_results[day] += count

        # Count weekday and weekend trips
        day_type_counts = chunk["day_type"].value_counts()

        # Add weekday/weekend counts to the dictionary
        for day_type, count in day_type_counts.items():

            # If the category does not exist yet, create it
            if day_type not in day_type_results:
                day_type_results[day_type] = 0

            # Add the current chunk's trips to that category
            day_type_results[day_type] += count

    # Calculate the average trip duration for the current file
    average_duration = total_duration / total_trips

    # Store the file name, trip count and average duration
    file_results.append({
        "file": file,
        "cleaned_trips": total_trips,
        "average_trip_duration": average_duration
    })

    # Display a short result for the completed file
    print("Cleaned trips:", total_trips)

    # Display the average trip duration
    print("Average duration:", round(average_duration, 2), "minutes")


# Convert file results into a DataFrame
taxi_file_summary = pd.DataFrame(file_results)

# Convert hourly results into a DataFrame
taxi_hour_summary = pd.DataFrame(
    list(hour_results.items()),
    columns=["hour", "trip_count"]
)

# Sort hourly results from hour 0 to hour 23
taxi_hour_summary = taxi_hour_summary.sort_values("hour")


# Convert day results into a DataFrame
taxi_day_summary = pd.DataFrame(
    list(day_results.items()),
    columns=["day_of_week", "trip_count"]
)


# Create the correct order for days of the week
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Convert day column into categorical order
taxi_day_summary["day_of_week"] = pd.Categorical(
    taxi_day_summary["day_of_week"],
    categories=day_order,
    ordered=True
)

# Sort days from Monday to Sunday
taxi_day_summary = taxi_day_summary.sort_values("day_of_week")


# Convert weekday/weekend results into a DataFrame
taxi_day_type_summary = pd.DataFrame(
    list(day_type_results.items()),
    columns=["day_type", "trip_count"]
)


# Save file-level results as CSV
taxi_file_summary.to_csv(
    "taxi_file_summary.csv",
    index=False
)

# Save hourly results as CSV
taxi_hour_summary.to_csv(
    "taxi_hour_summary.csv",
    index=False
)

# Save day-of-week results as CSV
taxi_day_summary.to_csv(
    "taxi_day_summary.csv",
    index=False
)

# Save weekday/weekend results as CSV
taxi_day_type_summary.to_csv(
    "taxi_day_type_summary.csv",
    index=False
)


# Find the hour with the highest number of trips
peak_hour_row = taxi_hour_summary.loc[
    taxi_hour_summary["trip_count"].idxmax()
]

# Find the busiest day
busiest_day_row = taxi_day_summary.loc[
    taxi_day_summary["trip_count"].idxmax()
]

# Calculate total trips
grand_total_trips = taxi_file_summary["cleaned_trips"].sum()

# Calculate weekday trips
weekday_trips = taxi_day_type_summary.loc[
    taxi_day_type_summary["day_type"] == "Weekday",
    "trip_count"
].sum()

# Calculate weekend trips
weekend_trips = taxi_day_type_summary.loc[
    taxi_day_type_summary["day_type"] == "Weekend",
    "trip_count"
].sum()


# Calculate weekday percentage
weekday_percentage = (
    weekday_trips / (weekday_trips + weekend_trips)
) * 100

# Calculate weekend percentage
weekend_percentage = (
    weekend_trips / (weekday_trips + weekend_trips)
) * 100


# Display the final project summary
# print("\n======================================")
# print("       NYC TAXI ANALYSIS SUMMARY")
# print("======================================")

# # Display total cleaned trips
# print("Total cleaned trips:", grand_total_trips)

# # Display peak hour
# print(
#     "Peak traffic hour:",
#     int(peak_hour_row["hour"]),
#     ":00"
# )

# # Display trips during peak hour
# print(
#     "Trips during peak hour:",
#     int(peak_hour_row["trip_count"])
# )

# # Display busiest day
# print(
#     "Busiest day:",
#     busiest_day_row["day_of_week"]
# )

# Display weekday percentage
# print(
#     "Weekday trips:",
#     round(weekday_percentage, 2),
#     "%"
# )

# # Display weekend percentage
# print(
#     "Weekend trips:",
#     round(weekend_percentage, 2),
#     "%"
# )

# Tell us that all summary files were created
# print("\nAnalysis completed successfully.")

# Display the names of the output files
# print("Created:")
# print("- taxi_file_summary.csv")
# print("- taxi_hour_summary.csv")
# print("- taxi_day_summary.csv")
# print("- taxi_day_type_summary.csv")




# Import matplotlib for creating charts
import matplotlib.pyplot as plt


# -------------------------------
# CHART 1: TRIPS BY HOUR
# -------------------------------

# # Create a figure for the hourly traffic chart
# plt.figure(figsize=(10, 5))

# # Create a bar chart using hour and trip count
# plt.bar(
#     taxi_hour_summary["hour"],
#     taxi_hour_summary["trip_count"]
# )

# # Add a title to the chart
# plt.title("NYC Taxi Trips by Hour")

# # Add a label to the X-axis
# plt.xlabel("Hour of Day")

# # Add a label to the Y-axis
# plt.ylabel("Number of Trips")

# # Show all 24 hours on the X-axis
# plt.xticks(range(24))

# # Adjust the chart layout
# plt.tight_layout()

# # Display the chart
# plt.show()


# # -------------------------------
# # CHART 2: TRIPS BY DAY
# # -------------------------------

# # Create a figure for the day-of-week chart
# plt.figure(figsize=(10, 5))

# # Create a bar chart using day and trip count
# plt.bar(
#     taxi_day_summary["day_of_week"].astype(str),
#     taxi_day_summary["trip_count"]
# )

# # Add a title to the chart
# plt.title("NYC Taxi Trips by Day of Week")

# # Add a label to the X-axis
# plt.xlabel("Day of Week")

# # Add a label to the Y-axis
# plt.ylabel("Number of Trips")

# # Rotate day names slightly for readability
# plt.xticks(rotation=30)

# # Adjust the chart layout
# plt.tight_layout()

# # Display the chart
# plt.show()


# # -------------------------------
# # CHART 3: WEEKDAY VS WEEKEND
# # -------------------------------

# # Create a figure for weekday/weekend comparison
# plt.figure(figsize=(7, 5))

# # Create a bar chart using day type and trip count
# plt.bar(
#     taxi_day_type_summary["day_type"],
#     taxi_day_type_summary["trip_count"]
# )

# # Add a title to the chart
# plt.title("Weekday vs Weekend Taxi Trips")

# # Add a label to the X-axis
# plt.xlabel("Day Type")

# # Add a label to the Y-axis
# plt.ylabel("Number of Trips")

# # Adjust the chart layout
# plt.tight_layout()

# # Display the chart
# plt.show()



# ============================================================
# TAXI CONGESTION ANALYSIS
# ============================================================

# Create a new dictionary to store total trip duration for each hour
hour_duration_results = {}

# Create a new dictionary to store total trip distance for each hour
hour_distance_results = {}

# Process all four taxi files again
for file in taxi_files:

#     # Display the current file being processed
#     print("\nProcessing for congestion:", file)

    # Read the taxi file in chunks to avoid using too much memory
    for chunk in pd.read_csv(
        file,
        chunksize=500000,
        usecols=[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "passenger_count",
            "trip_distance",
            "fare_amount"
        ]
    ):

    #     # Convert pickup time into datetime format
        chunk["pickup_time"] = pd.to_datetime(
            chunk["tpep_pickup_datetime"],
            errors="coerce"
        )

    #     # Convert drop-off time into datetime format
        chunk["dropoff_time"] = pd.to_datetime(
            chunk["tpep_dropoff_datetime"],
            errors="coerce"
        )

    #     # Calculate trip duration in minutes
        chunk["trip_duration"] = (
            chunk["dropoff_time"] - chunk["pickup_time"]
        ).dt.total_seconds() / 60

    #     # Keep only valid taxi trips
        chunk = chunk[
            chunk["pickup_time"].notna() &
            chunk["dropoff_time"].notna() &
            (chunk["trip_distance"] > 0) &
            (chunk["fare_amount"] > 0) &
            (chunk["passenger_count"] > 0) &
            (chunk["trip_duration"] > 0) &
            (chunk["trip_duration"] <= 1440)
        ]

        # Extract the pickup hour
        chunk["hour"] = chunk["pickup_time"].dt.hour

        # # Calculate total trip duration for each hour
        hourly_duration = chunk.groupby("hour")["trip_duration"].sum()

        # # Add hourly duration to the overall dictionary
        for hour, duration in hourly_duration.items():

        #     # Create the hour if it does not already exist
            if hour not in hour_duration_results:
                hour_duration_results[hour] = 0

        #     # Add the current chunk duration
            hour_duration_results[hour] += duration

        # # Calculate total trip distance for each hour
        hourly_distance = chunk.groupby("hour")["trip_distance"].sum()

        # # Add hourly distance to the overall dictionary
        for hour, distance in hourly_distance.items():

        #     # Create the hour if it does not already exist
            if hour not in hour_distance_results:
                hour_distance_results[hour] = 0

        #     # Add the current chunk distance
            hour_distance_results[hour] += distance


# Create a DataFrame containing hourly duration totals
hour_duration_summary = pd.DataFrame(
    list(hour_duration_results.items()),
    columns=["hour", "total_duration"]
)

# # Create a DataFrame containing hourly distance totals
hour_distance_summary = pd.DataFrame(
    list(hour_distance_results.items()),
    columns=["hour", "total_distance"]
)

# # Add total duration information to the existing hourly summary
taxi_hour_summary = taxi_hour_summary.merge(
    hour_duration_summary,
    on="hour"
)

# # Add total distance information to the hourly summary
taxi_hour_summary = taxi_hour_summary.merge(
    hour_distance_summary,
    on="hour"
)

# # Calculate average trip duration for each hour
taxi_hour_summary["avg_duration"] = (
    taxi_hour_summary["total_duration"] /
    taxi_hour_summary["trip_count"]
)

# # Calculate average trip distance for each hour
taxi_hour_summary["avg_distance"] = (
    taxi_hour_summary["total_distance"] /
    taxi_hour_summary["trip_count"]
)

# # Calculate average taxi speed in miles per hour
taxi_hour_summary["avg_speed"] = (
    taxi_hour_summary["avg_distance"] /
    taxi_hour_summary["avg_duration"]
) * 60

# # Calculate the overall average speed
overall_speed = taxi_hour_summary["avg_speed"].mean()

# # Classify each hour as Normal or High Congestion
taxi_hour_summary["congestion_level"] = taxi_hour_summary[
    "avg_speed"
].apply(
    lambda speed:
    "High Congestion" if speed < overall_speed else "Normal"
)

# # Save the congestion analysis into a CSV file
taxi_hour_summary.to_csv(
    "taxi_congestion_summary.csv",
    index=False
)

# # Find the hour with the lowest average speed
worst_hour = taxi_hour_summary.loc[
    taxi_hour_summary["avg_speed"].idxmin(),
    "hour"
]

# Find the lowest average speed
worst_speed = taxi_hour_summary["avg_speed"].min()

# Display the congestion analysis heading
# print("\n======================================")
# print("       TAXI CONGESTION ANALYSIS")
# print("======================================")

# # Display the most congested hour
# print(
#     "Most congested hour:",
#     int(worst_hour),
#     ":00"
# )

# # Display the lowest average speed
# print(
#     "Lowest average speed:",
#     round(worst_speed, 2),
#     "mph"
# )

# # Display the overall average speed
# print(
#     "Overall average speed:",
#     round(overall_speed, 2),
#     "mph"
# )

# Display confirmation that the file was created
# print("\nCreated:")
# print("- taxi_congestion_summary.csv")




