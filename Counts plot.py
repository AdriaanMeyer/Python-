import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Desktop/SQL/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Extract relevant columns from DataFrame
x_column = 'Age'

# Seaborn countplot
sns.countplot(x=x_column, data=df)

# Matplotlib customization
plt.title('Count of Observations for Each Value')
plt.xlabel(x_column)
plt.ylabel('Count')
plt.show()
