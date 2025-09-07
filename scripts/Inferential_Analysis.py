import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency, pearsonr

# Define the file paths for the datasets
DATASET1_PATH = "../data/dataset1.csv"
DATASET2_PATH = "../data/dataset2.csv"
OUTPUT_PATH = "../results/final_inferential_results.txt"

# --- Main Function to Run All Tests ---
def run_all_tests():
    """
    Loads the datasets and performs all three key inferential tests.
    The results are printed to the console and saved to a text file.
    """
    try:
        # Load the datasets
        df1 = pd.read_csv(DATASET1_PATH)
        df2 = pd.read_csv(DATASET2_PATH)

        # Create a text file to save the results
        with open(OUTPUT_PATH, 'w') as f:
            f.write("===== Final Inferential Analysis Results =====\n\n")

            # --- Test 1: Pearson Correlation ---
            # Hypothesis: There is a negative correlation between rat arrival and bat landings.
            # This is a key part of the project's hypothesis.
            f.write("--- Pearson Correlation Test ---\n")
            print("\n--- Pearson Correlation Test ---")
            
            # Perform the Pearson correlation test on the two continuous variables.
            correlation, p_value = pearsonr(df2['bat_landing_number'], df2['rat_arrival_number'])
            
            f.write(f"Correlation Coefficient (r): {correlation:.4f}\n")
            f.write(f"P-value: {p_value:.4f}\n\n")
            print(f"Correlation Coefficient (r): {correlation:.4f}")
            print(f"P-value: {p_value:.4f}\n")

            # --- Test 2: T-Test ---
            # Hypothesis: Bats take longer to land on food when a rat is present.
            # We compare 'bat_landing_to_food' for two groups: with and without rat presence.
            f.write("--- T-Test ---\n")
            print("--- T-Test ---")
            
            # Define the two groups based on the presence of rats.
            # A value of 0 for 'seconds_after_rat_arrival' means no rat was present.
            group_with_rat = df1[df1['seconds_after_rat_arrival'] > 0]['bat_landing_to_food'].dropna()
            group_without_rat = df1[df1['seconds_after_rat_arrival'] == 0]['bat_landing_to_food'].dropna()
            
            # Perform the T-test.
            t_stat, p_value_ttest = ttest_ind(group_with_rat, group_without_rat, equal_var=False)
            
            f.write(f"T-statistic: {t_stat:.4f}\n")
            f.write(f"P-value: {p_value_ttest:.4f}\n\n")
            print(f"T-statistic: {t_stat:.4f}")
            print(f"P-value: {p_value_ttest:.4f}\n")

            # --- Test 3: Chi-squared Test ---
            # Hypothesis: There is an association between 'risk' and 'reward'.
            # This demonstrates that the two categorical variables are not independent.
            f.write("--- Chi-Squared Test ---\n")
            print("--- Chi-Squared Test ---")
            
            # Create a contingency table from the two categorical variables.
            contingency_table = pd.crosstab(df1['risk'], df1['reward'])
            
            # Perform the Chi-squared test.
            chi2_stat, p_value_chi2, dof, expected = chi2_contingency(contingency_table)
            
            f.write(f"Chi-squared statistic: {chi2_stat:.4f}\n")
            f.write(f"P-value: {p_value_chi2:.4f}\n\n")
            print(f"Chi-squared statistic: {chi2_stat:.4f}")
            print(f"P-value: {p_value_chi2:.4f}\n")

            f.write("All results saved to final_inferential_results.txt\n")
            print("All results saved to final_inferential_results.txt")

    except FileNotFoundError as e:
        print(f"Error: One or more datasets not found. Please check your file paths: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_all_tests()
