import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/Python-/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Set the relevant column
y_column = '2 Week Anti S Results'

# Create a box and whiskers chart for 2 Week Anti S Results
sns.boxplot(y=df[y_column])
plt.title('Box and Whiskers Chart - 2 Week Anti S Results')
plt.ylabel('2 Week Anti S Results')
plt.show()
