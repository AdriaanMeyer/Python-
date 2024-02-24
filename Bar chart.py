import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Desktop/SQL/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Extract relevant columns from DataFrame
x_column = 'Staff Number'
y_column = '2 Week Anti S Results'

# Seaborn horizontal barplot
sns.barplot(x=y_column, y=x_column, data=df, orient='h')

# Matplotlib customization
plt.title('Horizontal Bar Chart Example')
plt.xlabel(y_column)
plt.ylabel(x_column)
plt.show()

