# Import pandas for data analysis
import pandas as pd


# Store the names of the 4 NYC taxi files
files = [
    "nyc_yellow/yellow_tripdata_2015-01.csv",
    "nyc_yellow/yellow_tripdata_2016-01.csv",
    "nyc_yellow/yellow_tripdata_2016-02.csv",
    "nyc_yellow/yellow_tripdata_2016-03.csv"
]


# Store hourly results from all chunks
all_results = []


# Store the low-congestion reference data
all_reference = []


# ---------------------------------------------------------
# STEP 1: Read all files and collect reference data
# ---------------------------------------------------------

for file in files:

    # Read the taxi file in chunks of 100,000 rows
    for df in pd.read_csv(
        file,
        usecols=[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_distance"
        ],
        chunksize=100000
    ):

        # Convert pickup time to datetime
        df["tpep_pickup_datetime"] = pd.to_datetime(
            df["tpep_pickup_datetime"],
            errors="coerce"
        )

        # Convert dropoff time to datetime
        df["tpep_dropoff_datetime"] = pd.to_datetime(
            df["tpep_dropoff_datetime"],
            errors="coerce"
        )

        # Calculate actual travel time in minutes
        df["actual_time"] = (
            df["tpep_dropoff_datetime"]
            - df["tpep_pickup_datetime"]
        ).dt.total_seconds() / 60

        # Extract pickup hour
        df["hour"] = df["tpep_pickup_datetime"].dt.hour

        # Remove invalid travel times and distances
        df = df[
            (df["actual_time"] > 1) &
            (df["actual_time"] <= 180) &
            (df["trip_distance"] > 0) &
            (df["trip_distance"] <= 100)
        ]

        # Create distance groups rounded to the nearest mile
        df["distance_group"] = df["trip_distance"].round()

        # Select the low-congestion reference period
        reference = df[df["hour"].between(0, 5)]

        # Keep only the columns required for the baseline
        all_reference.append(
            reference[
                ["distance_group", "actual_time"]
            ]
        )


# ---------------------------------------------------------
# STEP 2: Create ONE global expected travel-time baseline
# ---------------------------------------------------------

# Combine reference data from all files and chunks
reference_data = pd.concat(
    all_reference,
    ignore_index=True
)


# Calculate expected travel time for each distance group
baseline = reference_data.groupby(
    "distance_group"
)["actual_time"].mean().reset_index()


# Rename actual_time as expected_time
baseline = baseline.rename(
    columns={
        "actual_time": "expected_time"
    }
)


# ---------------------------------------------------------
# STEP 3: Process all taxi data again
# ---------------------------------------------------------

for file in files:

    # Read the file again in chunks
    for df in pd.read_csv(
        file,
        usecols=[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_distance"
        ],
        chunksize=100000
    ):

        # Convert pickup time to datetime
        df["tpep_pickup_datetime"] = pd.to_datetime(
            df["tpep_pickup_datetime"],
            errors="coerce"
        )

        # Convert dropoff time to datetime
        df["tpep_dropoff_datetime"] = pd.to_datetime(
            df["tpep_dropoff_datetime"],
            errors="coerce"
        )

        # Calculate actual travel time
        df["actual_time"] = (
            df["tpep_dropoff_datetime"]
            - df["tpep_pickup_datetime"]
        ).dt.total_seconds() / 60

        # Extract pickup hour
        df["hour"] = df["tpep_pickup_datetime"].dt.hour

        # Remove invalid records
        df = df[
            (df["actual_time"] > 1) &
            (df["actual_time"] <= 180) &
            (df["trip_distance"] > 0) &
            (df["trip_distance"] <= 100)
        ]

        # Create the same distance groups
        df["distance_group"] = df["trip_distance"].round()

        # Attach the GLOBAL expected travel time
        df = df.merge(
            baseline,
            on="distance_group",
            how="left"
        )

        # Calculate delay ratio
        df["delay_ratio"] = (
            df["actual_time"] /
            df["expected_time"]
        )

        # Remove records without a valid expected time
        df = df[
            df["expected_time"].notna() &
            (df["expected_time"] > 0)
        ]

        # Calculate hourly results
        summary = df.groupby("hour").agg(
            trips=("delay_ratio", "count"),
            average_actual_time=("actual_time", "mean"),
            average_expected_time=("expected_time", "mean"),
            average_delay_ratio=("delay_ratio", "mean")
        ).reset_index()

        # Store the chunk result
        all_results.append(summary)


# ---------------------------------------------------------
# STEP 4: Combine all chunk results
# ---------------------------------------------------------

result = pd.concat(
    all_results,
    ignore_index=True
)


# Combine results for the same hour
result = result.groupby("hour").agg(
    trips=("trips", "sum"),
    average_actual_time=("average_actual_time", "mean"),
    average_expected_time=("average_expected_time", "mean"),
    average_delay_ratio=("average_delay_ratio", "mean")
).reset_index()


# Sort hours from 0 to 23
result = result.sort_values("hour")


# ---------------------------------------------------------
# STEP 5: Save the final CSV
# ---------------------------------------------------------

result.to_csv(
    "delay_ratio_summary.csv",
    index=False
)


# Find the hour with the highest delay ratio
highest_delay = result.loc[
    result["average_delay_ratio"].idxmax()
]


# Print completion message
print("\nDelay Ratio Analysis Completed!")


# Print hourly results
print("\nHourly Delay Ratio:")
print(result)


# Print highest delay-ratio hour
print(
    "\nHighest delay ratio hour:",
    int(highest_delay["hour"])
)


# Print highest delay ratio
print(
    "Highest delay ratio:",
    round(
        highest_delay["average_delay_ratio"],
        2
    )
)