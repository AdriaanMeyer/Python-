import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/Python-/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Print column names
print(df.columns)

# Extract relevant columns from DataFrame
x_column = '2 Week Anti S Results'
y_column = '4 Week Anti S Results'  # Corrected column name

# Seaborn scatterplot
sns.scatterplot(x=df[x_column], y=df[y_column], label='Data Points')

# Matplotlib customization
plt.title('Anti-S Correlation')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.legend()
plt.show()