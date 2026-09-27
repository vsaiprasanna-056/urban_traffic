# Import pandas for data analysis
import pandas as pd


# List the four NYC taxi files
files = [
    "nyc_yellow/yellow_tripdata_2015-01.csv",
    "nyc_yellow/yellow_tripdata_2016-01.csv",
    "nyc_yellow/yellow_tripdata_2016-02.csv",
    "nyc_yellow/yellow_tripdata_2016-03.csv"
]


# Create an empty list to store zone results
all_results = []


# Process each taxi file
for file in files:

    # Read the file in small chunks
    for df in pd.read_csv(
        file,
        usecols=[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_distance",
            "pickup_latitude",
            "pickup_longitude"
        ],
        chunksize=100000
    ):

        # Convert pickup time into datetime
        df["tpep_pickup_datetime"] = pd.to_datetime(
            df["tpep_pickup_datetime"],
            errors="coerce"
        )

        # Convert dropoff time into datetime
        df["tpep_dropoff_datetime"] = pd.to_datetime(
            df["tpep_dropoff_datetime"],
            errors="coerce"
        )

        # Calculate travel time in minutes
        df["travel_time"] = (
            df["tpep_dropoff_datetime"]
            - df["tpep_pickup_datetime"]
        ).dt.total_seconds() / 60

        # Remove invalid trips
        df = df[
            (df["travel_time"] > 1) &
            (df["travel_time"] <= 180) &
            (df["trip_distance"] > 0) &
            (df["trip_distance"] <= 100) &
            (df["pickup_latitude"] != 0) &
            (df["pickup_longitude"] != 0)
        ]

        # Create latitude grid values
        df["lat_zone"] = df["pickup_latitude"].round(2)

        # Create longitude grid values
        df["lon_zone"] = df["pickup_longitude"].round(2)

        # Create a zone name
        df["zone"] = (
            df["lat_zone"].astype(str)
            + "_"
            + df["lon_zone"].astype(str)
        )

        # Calculate average speed in mph
        df["average_speed"] = (
            df["trip_distance"]
            / df["travel_time"]
            * 60
        )

        # Keep only realistic speeds
        df = df[
            (df["average_speed"] > 0) &
            (df["average_speed"] <= 80)
        ]

        # Group the trips by geographic zone
        zone_summary = df.groupby("zone").agg(
            trip_count=("travel_time", "count"),
            average_travel_time=("travel_time", "mean"),
            average_speed=("average_speed", "mean"),
            average_distance=("trip_distance", "mean")
        ).reset_index()

        # Store this chunk's result
        all_results.append(zone_summary)


# Combine all chunk-level results
result = pd.concat(
    all_results,
    ignore_index=True
)


# Combine repeated zones from different chunks
result = result.groupby("zone").agg(
    trip_count=("trip_count", "sum"),
    average_travel_time=("average_travel_time", "mean"),
    average_speed=("average_speed", "mean"),
    average_distance=("average_distance", "mean")
).reset_index()


# Keep only zones with at least 100 trips
# This removes very small areas from the analysis
result = result[
    result["trip_count"] >= 100
]


# Create a congestion score
# Lower speed means higher congestion
result["congestion_score"] = (
    1 / result["average_speed"]
)


# Sort the zones by congestion score
result = result.sort_values(
    "congestion_score",
    ascending=False
)


# Save the zone-level congestion result
result.to_csv(
    "zone_congestion_summary.csv",
    index=False
)


# Display the top 10 most congested zones
print("\nTop 10 Congested Zones:")

print(
    result[
        [
            "zone",
            "trip_count",
            "average_travel_time",
            "average_speed",
            "average_distance"
        ]
    ].head(10)
)


# Print completion message
print("\nZone-level congestion analysis completed!")

# Print the output file name
print(
    "Output file: zone_congestion_summary.csv"
)