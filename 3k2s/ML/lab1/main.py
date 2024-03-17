import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("df\\tips.csv")

df = pd.DataFrame(data)

def calculate_z_scores(df):
    z_scores = {}
    for column in df.select_dtypes(include=[np.number]).columns:
        column_data = df[column].dropna()
        mean = np.mean(column_data)
        std_dev = np.std(column_data, ddof=1)
        z_scores[column] = (column_data - mean) / std_dev
    return z_scores

z_scores = calculate_z_scores(df)


for column, scores in z_scores.items():
    df[f'{column}_z-score'] = scores
    print(f"Z-scores for {column} (first 5 values):\n", scores.head())

df_z_scores = pd.DataFrame(z_scores).abs()

df['agg_z_score'] = df_z_scores.mean(axis=1)

# Identify outliers based on the aggregated z-score
outliers_threshold = max(1,df['agg_z_score'].nlargest(9).iloc[-1])
outliers = df[df['agg_z_score'] > outliers_threshold]
non_outliers = df[df['agg_z_score'] <= outliers_threshold]

# Visualize the dataset with outliers highlighted
fig = plt.figure(figsize=(10, 7))

# 3D scatter plot
ax = fig.add_subplot(111, projection='3d')
ax.scatter(non_outliers['total_bill'], non_outliers['tip'], non_outliers['size'], color='blue', label='Regular data')
ax.scatter(outliers['total_bill'], outliers['tip'], outliers['size'], color='red', label='Outliers')

ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
ax.set_zlabel('Size')
ax.legend()

plt.show()
