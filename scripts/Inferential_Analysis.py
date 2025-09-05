#Inferential_Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind, chi2_contingency

# ============================
# PART 1: DATA CLEANING & PREPARATION
# ============================

# --- Cleaning dataset2 ---
print("--- Cleaning Dataset 2 ---")
dataset2 = pd.read_csv("dataset2.csv")
print("Dataset2 is loaded successfully!")

# Fill missing values
for col in dataset2.columns:
    if dataset2[col].dtype == 'object':
        most_common = dataset2[col].mode()[0]
        dataset2[col] = dataset2[col].fillna(most_common)
    else:
        average_val = dataset2[col].mean()
        dataset2[col] = dataset2[col].fillna(average_val)

# Remove duplicates
dataset2 = dataset2.drop_duplicates()

# Clean column names
dataset2.columns = dataset2.columns.str.strip().str.lower().str.replace(' ', '_')

# Save the cleaned dataset
dataset2.to_csv("clean_dataset2.csv", index=False)
print("Dataset2 cleaned and saved as 'clean_dataset2.csv'\n")

# --- Cleaning dataset1 ---
print("--- Cleaning Dataset 1 ---")
dataset1 = pd.read_csv('dataset1.csv') # Assuming this is your original dataset1
print("Dataset1 is loaded successfully!")

# Handling missing data. The original code uses .dropna()
dataset1_cleaned = dataset1.dropna()
dataset1_cleaned.columns = dataset1_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')

# Save the cleaned dataset
dataset1_cleaned.to_csv("dataset1_cleaned.csv", index=False)
print("Dataset1 cleaned and saved as 'dataset1_cleaned.csv'\n")

# ============================
# PART 2: DESCRIPTIVE ANALYSIS
# ============================
print("--- Performing Descriptive Analysis ---")

# --- Descriptive for dataset2 ---
df2 = pd.read_csv("clean_dataset2.csv")
print("\nDescriptive statistics for Dataset 2:")
print(df2.describe())

# Histograms for continuous variables in dataset2
df2.hist(figsize=(12, 8), bins=30)
plt.suptitle("Distribution of Features in Dataset 2")
plt.show()

# --- Descriptive for dataset1 ---
df1 = pd.read_csv('dataset1_cleaned.csv')
print("\nDescriptive statistics for Dataset 1:")
print(df1.describe(include='all'))

# Bar chart for 'habit' distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='habit', data=df1)
plt.title("Habit Distribution")
plt.show()

# Boxplot for outlier detection in 'bat_landing_to_food'
plt.figure(figsize=(8, 5))
sns.boxplot(x=df1['bat_landing_to_food'])
plt.title("Outlier Check: Bat Landing to Food")
plt.show()

# ============================
# PART 3: INFERENTIAL ANALYSIS
# ============================
print("\n--- Performing Inferential Analysis ---")

# --- Analysis using Dataset 2: Correlation ---
# This tests if more rat arrivals correlate with fewer bat landings.
correlation, p_value = pearsonr(df2['rat_arrival_number'], df2['bat_landing_number'])

print("\n--- Correlation Analysis (Dataset 2) ---")
print(f"Pearson Correlation between Bat Landings and Rat Arrivals: {correlation:.2f}")
print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("Result: Significant relationship found. We reject the null hypothesis.")
    if correlation < 0:
        print("Interpretation: As rat arrivals increase, bat landings tend to decrease. This supports the predation risk hypothesis.")
    else:
        print("Interpretation: As rat arrivals increase, bat landings also tend to increase. This does not support the predation risk hypothesis.")
else:
    print("Result: No significant relationship found. We fail to reject the null hypothesis.")
    print("Interpretation: The number of bat landings does not appear to be significantly correlated with the number of rat arrivals.")
print("-" * 30)

# --- Analysis using Dataset 1: T-test ---
# This tests if vigilance (bat_landing_to_food) is different based on rat presence duration.
df1['rat_present_dummy'] = df1['seconds_after_rat_arrival'].apply(lambda x: 1 if x > 0 else 0)

# Separate data for t-test
times_with_rats = df1[df1['rat_present_dummy'] == 1]['bat_landing_to_food'].dropna()
times_without_rats = df1[df1['rat_present_dummy'] == 0]['bat_landing_to_food'].dropna()

t_stat, p_value = ttest_ind(times_with_rats, times_without_rats, equal_var=False)

print("--- T-Test Analysis (Dataset 1) ---")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("Result: Significant difference found. We reject the null hypothesis.")
    print(f"Mean time with rats: {times_with_rats.mean():.2f}s")
    print(f"Mean time without rats: {times_without_rats.mean():.2f}s")
    print("Interpretation: Bats take a significantly different amount of time to approach food when rats are present. If the time is longer, it suggests increased vigilance.")
else:
    print("Result: No significant difference found. We fail to reject the null hypothesis.")
    print("Interpretation: Bat landing to food time does not appear to be significantly different when rats are present.")
print("-" * 30)

# --- Analysis using Dataset 1: Chi-squared test for categorical variables ---
# This tests if there is an association between 'risk' behavior and rat presence.
contingency_table = pd.crosstab(df1['risk'], df1['rat_present_dummy'])

chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

print("--- Chi-squared Test (Dataset 1) ---")
print(f"Chi-squared statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("Result: Significant association found. We reject the null hypothesis.")
    print("Interpretation: There is a significant relationship between a bat's risk-taking behavior and the presence of rats. ")
else:
    print("Result: No significant association found. We fail to reject the null hypothesis.")
    print("Interpretation: A bat's risk-taking behavior does not appear to be associated with the presence of rats.")
print("-" * 30)

print("\nAnalysis Complete! ")
