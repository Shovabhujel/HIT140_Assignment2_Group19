# Data Cleaning_Shova (Dataset2)

import pandas as ps  # 1. Handle data in tables

dataset2 = ps.read_csv("dataset2.csv") # 2. Load the dataset
print("Dataset2 is loaded successfully! Let's clean it.\n")

print("Let's check if there are missing values in the dataset:") # 3. Checking for missing data in each column
print(dataset2.isnull().sum(), "\n")

print("--- Filling missing values ---") # 3. Fill missing values
for col in dataset2.columns:
    if dataset2[col].dtype == 'object':
        # Fill missing text values with the most common value
        most_common = dataset2[col].mode()[0]
        dataset2[col] = dataset2[col].fillna(most_common)
        print(f"Filled missing values in '{col}' with most common value: {most_common}")
    else:
        # Fill missing numeric values with the average
        average_val = dataset2[col].mean()
        dataset2[col] = dataset2[col].fillna(average_val)
        print(f"Filled numeric column '{col}' with average value: {average_val:.2f}")

print("\nMissing values after cleaning:")
print(dataset2.isnull().sum(), "\n")

duplicates = dataset2.duplicated().sum() #4. Remove duplicates
print(f"Found {duplicates} duplicate rows. Removing them now...")
dataset2 = dataset2.drop_duplicates()
print("Duplicates removed.\n")

dataset2.columns = dataset2.columns.str.strip().str.lower().str.replace(' ', '_') #5. Clean column names
print("Column names cleaned and standardized:")
print(dataset2.columns, "\n")

dataset2.to_csv("clean_dataset2.csv", index=False) #6. Save the cleaned dataset
print("Dataset2 cleaned and saved as 'clean_dataset2.csv'")
