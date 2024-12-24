import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:/Users/JAYESH PC/Desktop/Python/tips.csv'  # Update this to your file path
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}. Check the file path and try again.")
    exit()

# Display dataset information
print("Dataset Information:")
data.info()
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

# Check for missing values and handle them
if data.isnull().sum().any():
    print("\nNote: There are missing values in the dataset. Filling them with column means.")
    data.fillna(data.mean(numeric_only=True), inplace=True)

# Basic analysis: Calculate averages for total bill and tip
try:
    average_total_bill = data['total_bill'].mean()
    average_tip = data['tip'].mean()
    print(f"\nAverage Total Bill: ${round(average_total_bill, 2)}")
    print(f"Average Tip: ${round(average_tip, 2)}")
except KeyError as e:
    print(f"Error: Column {e} is missing. Make sure the dataset includes 'total_bill' and 'tip'.")
    exit()

# Visualization: Average tip by day
try:
    avg_tip_by_day = data.groupby('day')['tip'].mean()
    plt.figure(figsize=(8, 6))
    avg_tip_by_day.plot(kind='bar', color='skyblue')
    plt.title('Average Tip by Day')
    plt.xlabel('Day')
    plt.ylabel('Average Tip ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except KeyError as e:
    print(f"Error: Column {e} is missing. Make sure the dataset includes 'day' and 'tip'.")

# Visualization: Scatter plot of total bill vs tip
try:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='total_bill', y='tip', hue='sex', style='smoker', s=100)
    plt.title('Total Bill vs Tip')
    plt.xlabel('Total Bill ($)')
    plt.ylabel('Tip ($)')
    plt.legend(title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
except KeyError as e:
    print(f"Error: Column {e} is missing. Make sure the dataset includes 'total_bill', 'tip', 'sex', and 'smoker'.")

# Visualization: Heatmap of correlations
plt.figure(figsize=(8, 6))
correlation_matrix = data.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Insights from the data
print("\nInsights:")
print(f"1. The average total bill is ${round(average_total_bill, 2)}, and the average tip is ${round(average_tip, 2)}.")
print("2. The bar chart shows that tipping behavior varies by day, which could help with operational planning.")
print("3. The scatter plot indicates a positive relationship between total bill and tip, with differences influenced by gender and smoking status.")
print("4. The heatmap confirms a strong correlation between total bill and tip, among other numerical variables.")
