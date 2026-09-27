# # Import pandas for data analysis.
# import pandas as pd

# # Import glob to automatically find all CSV files.
# import glob

# # Find all CSV files inside the uber_pickup folder.
# uber_files = glob.glob("uber_pickup/*.csv")

# # Create an empty list to store analysis results.
# results = []

# # Create an empty list to store files that do not have Date/Time.
# skipped_files = []

# # Process every CSV file one by one.
# for file in uber_files:

#     # Print the name of the file currently being processed.
#     print("\nProcessing:", file)

#     # Read the current CSV file using latin1 encoding.
#     df = pd.read_csv(file, encoding="latin1")

#     # Check whether the file contains the Date/Time column.
#     if "Date/Time" in df.columns:

#         # Convert Date/Time values into proper datetime format.
#         df["Date/Time"] = pd.to_datetime(
#             df["Date/Time"],
#             errors="coerce"
#         )

#         # Remove rows where Date/Time could not be converted.
#         df = df.dropna(subset=["Date/Time"])

#         # Count the total number of pickups.
#         total_pickups = len(df)

#         # Find the hour with the highest number of pickups.
#         peak_hour = df["Date/Time"].dt.hour.value_counts().idxmax()

#         # Find the busiest day of the week.
#         busiest_day = df["Date/Time"].dt.day_name().value_counts().idxmax()

#         # Check whether the Base column exists.
#         if "Base" in df.columns:

#             # Find the Uber base with the highest number of pickups.
#             top_base = df["Base"].value_counts().idxmax()

#         # If Base does not exist, store Not available.
#         else:
#             top_base = "Not available"

#         # Store the analysis results for this file.
#         results.append({
#             "file": file,
#             "total_pickups": total_pickups,
#             "peak_hour": peak_hour,
#             "busiest_day": busiest_day,
#             "top_base": top_base
#         })

#         # Print that this file was successfully analyzed.
#         print("Analyzed successfully.")

#     # If Date/Time column does not exist.
#     else:

#         # Add this file to the skipped files list.
#         skipped_files.append(file)

#         # Display the columns available in this file.
#         print("Date/Time column not found.")

#         # Display the available column names.
#         print("Columns:", list(df.columns))

#     # Delete the dataframe to save memory.
#     del df

# # Convert the successful results into a DataFrame.
# uber_summary = pd.DataFrame(results)

# # Save the successful analysis results into a CSV file.
# uber_summary.to_csv(
#     "uber_summary.csv",
#     index=False
# )

# # Display the final analysis heading.
# print("\n==============================")

# # Display the project section name.
# print("       UBER PICKUP ANALYSIS")

# # Display the closing line.
# print("==============================")

# # Display the successful analysis results.
# print(uber_summary)

# # Display the total number of CSV files found.
# print("\nTotal CSV files found:", len(uber_files))

# # Display the number of files successfully analyzed.
# print("Files analyzed:", len(results))

# # Display the number of files that were skipped.
# print("Files skipped:", len(skipped_files))

# # Display the skipped files if any exist.
# if skipped_files:

#     # Display the skipped-file heading.
#     print("\nSkipped files:")

#     # Print every skipped file name.
#     for file in skipped_files:

#         # Display the skipped file.
#         print(file)

# # Confirm that the output file was created.
# # print("\nCreated: uber_summary.csv")







# # Import pandas for reading CSV files.
# import pandas as pd

# # Import glob to find CSV files.
# import glob

# # Find all CSV files inside the Uber folder.
# uber_files = glob.glob("uber_pickup/*.csv")

# # Check every CSV file one by one.
# for file in uber_files:

#     # Read the current CSV file using latin1 encoding.
#     df = pd.read_csv(file, encoding="latin1", nrows=5)

#     # Check whether Date/Time is missing.
#     if "Date/Time" not in df.columns:

#         # Print the file name.
#         print("\nFile:", file)

#         # Print the column names.
#         print("Columns:", list(df.columns))

#     # Delete the dataframe to save memory.
#     del df


# Import pandas for data analysis.
import pandas as pd

# Store the path of the Uber Jan-Feb FOIL file.
foil_file = "uber_pickup/Uber-Jan-Feb-FOIL.csv"

# Store the path of the FHV services file.
fhv_file = "uber_pickup/other-FHV-services_jan-aug-2015.csv"


# ==============================
# UBER JAN-FEB FOIL ANALYSIS
# ==============================

# Read the Uber Jan-Feb FOIL CSV file using latin1 encoding.
foil = pd.read_csv(foil_file, encoding="latin1")

# Convert the date column into proper date format.
foil["date"] = pd.to_datetime(
    foil["date"],
    errors="coerce"
)

# Remove rows where the date is missing.
foil = foil.dropna(subset=["date"])

# Calculate the total number of trips.
total_foil_trips = foil["trips"].sum()

# Calculate the total number of active vehicles.
total_foil_vehicles = foil["active_vehicles"].sum()

# Find the date with the highest number of trips.
peak_foil_date = foil.loc[
    foil["trips"].idxmax(),
    "date"
]

# Find the highest number of trips recorded on one date.
peak_foil_trips = foil["trips"].max()

# Display the Uber Jan-Feb analysis heading.
print("\n==============================")

# Display the analysis name.
print("    UBER JAN-FEB DEMAND")

# Display the closing line.
print("==============================")

# Display the total trips.
print("Total trips:", total_foil_trips)

# Display the total active vehicles.
print("Total active vehicles:", total_foil_vehicles)

# Display the peak date.
print("Peak demand date:", peak_foil_date.date())

# Display the peak number of trips.
print("Peak trips on one date:", peak_foil_trips)


# ==============================
# FHV SERVICES ANALYSIS
# ==============================

# Read the FHV services CSV file using latin1 encoding.
fhv = pd.read_csv(fhv_file, encoding="latin1")

# Convert the pickup date column into proper date format.
fhv["Pick Up Date"] = pd.to_datetime(
    fhv["Pick Up Date"],
    errors="coerce"
)

# Remove rows where the pickup date is missing.
fhv = fhv.dropna(subset=["Pick Up Date"])

# Convert Number of Trips from text into numbers.
fhv["Number of Trips"] = pd.to_numeric(
    fhv["Number of Trips"],
    errors="coerce"
)

# Convert Number of Vehicles from text into numbers.
fhv["Number of Vehicles"] = pd.to_numeric(
    fhv["Number of Vehicles"],
    errors="coerce"
)

# Calculate the total number of FHV trips.
total_fhv_trips = fhv["Number of Trips"].sum()

# Calculate the total number of vehicles.
total_fhv_vehicles = fhv["Number of Vehicles"].sum()

# Find the base with the highest number of trips.
top_fhv_base = fhv.loc[
    fhv["Number of Trips"].idxmax(),
    "Base Name"
]

# Find the highest number of trips recorded for a base.
top_fhv_trips = fhv["Number of Trips"].max()

# Display the FHV analysis heading.
print("\n==============================")

# Display the analysis name.
print("       FHV ANALYSIS")

# Display the closing line.
print("==============================")

# Display the total FHV trips.
print("Total FHV trips:", total_fhv_trips)

# Display the total FHV vehicles.
print("Total FHV vehicles:", total_fhv_vehicles)

# Display the busiest FHV base.
print("Top FHV base:", top_fhv_base)

# Display the highest trips for a base.
print("Highest trips:", top_fhv_trips)

# Display completion message.
print("\nAdditional demand analysis completed.")