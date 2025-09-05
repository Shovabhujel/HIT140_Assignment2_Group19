import pandas as pd
import os

folder_path = "C:/Users/dell/OneDrive/Desktop/datasets"
file_out = "dataset1_cleaned.csv"  # output file name

# loading datasets
df1 = pd.read_csv(os.path.join(folder_path, "dataset1.csv"))
df2 = pd.read_csv(os.path.join(folder_path, "dataset2.csv"))

# first few rows of dataset1 and dataset2
print("Dataset 1:")
print(df1.head(), "\n")

print("Dataset 2:")
print(df2.head(), "\n")

# Summaries of both datasets
print("Dataset 1 summary:")
print(df1.describe(include="all"), "\n")

print("Dataset 2 summary:")
print(df2.describe(include="all"), "\n")



# Cleaning dataset1
print("\nPerforming cleaning steps on Dataset1...\n")

# Parse date/time
for col in ['start_time', 'rat_period_start', 'rat_period_end', 'sunset_time']:
    if col in df1.columns:
        df1[col] = pd.to_datetime(df1[col], dayfirst=True, errors='coerce')

# Convert numeric columns
for col in ['bat_landing_to_food', 'seconds_after_rat_arrival', 'hours_after_sunset']:
    if col in df1.columns:
        df1[col] = pd.to_numeric(df1[col], errors='coerce')

# Drop rows with missing critical values
df1 = df1.dropna(subset=[c for c in ['seconds_after_rat_arrival', 'bat_landing_to_food'] if c in df1.columns])

# Remove duplicates
df1 = df1.drop_duplicates()

# Remove impossible negative values
if 'seconds_after_rat_arrival' in df1.columns:
    df1 = df1[df1['seconds_after_rat_arrival'] >= 0]

# Standardize text columns
for col in ['habit', 'season']:
    if col in df1.columns:
        df1[col] = df1[col].astype(str).str.strip().str.lower()

# Reset index
df1 = df1.reset_index(drop=True)

# After cleaning summary
print("\n after cleaning (Dataset1)")
print(f"Shape after cleaning: {df1.shape[0]} rows × {df1.shape[1]} columns\n")

# Missing values per column
print("Missing values per column (after cleaning):")
print(df1.isna().sum(), "\n")

# Duplicate rows
print("Duplicate rows (after cleaning):", df1.duplicated().sum(), "\n")

# First 10 rows after cleaning dataset1
print("Dataset1 — First 10 Rows (After Cleaning)\n")
print(df1.head(10).to_string(index=False))

# Save cleaned file
df1.to_csv(os.path.join(folder_path, file_out), index=False)
print(f"\n File saved as {file_out}")
