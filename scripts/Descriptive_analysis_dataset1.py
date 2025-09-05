#Descriptive_analysis_and_key_visualization_dataset1 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Load the dataset 
df1 = pd.read_csv('dataset1_cleaned.csv') 
df1.head() 
df1.info() 


desc_stats = { 
    "mean": df1.mean(numeric_only=True), 
    "median": df1.median(numeric_only=True), 
    "mode": df1.mode(numeric_only=True).iloc[0], 
    "std_dev": df1.std(numeric_only=True), 
    "min": df1.min(numeric_only=True), 
    "max": df1.max(numeric_only=True), 
    "Q1": df1.quantile(0.25, numeric_only=True), 
    "Q3": df1.quantile(0.75, numeric_only=True) 
} 





# Bar chart for categorical variable 'habit' 
sns.countplot(x='habit', data=df1) 
plt.title("Habit Distribution") 
plt.show() 

# Histogram for numerical column 
df1['seconds_after_rat_arrival'].hist(bins=30) 
plt.title("Seconds After Rat Arrival") 
plt.show() 

# Boxplot for outlier detection 
sns.boxplot(x=df['bat_landing_to_food']) 
plt.title("Outlier Check: bat_landing_to_food") 
plt.show() 

# Pie chart for 'season' 
df1['season'].value_counts().plot.pie(autopct='%1.1f%%') 
plt.title("Season Proportions") 
plt.ylabel("") 
plt.show() 


df_cleaned = df.dropna()  # or use imputation 
df_cleaned.to_csv("dataset1_cleaned.csv", index=False) 

df1.describe()
