import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os

# Assuming the archive is already extracted and the CSV files are located in "/mnt/data/archive/"
directory_path = "/mnt/data/archive/"

# Loading the datasets
df_player_info = pd.read_csv(os.path.join(directory_path, 'ittf_player_info.csv'))
df_rankings = pd.read_csv(os.path.join(directory_path, 'ittf_rankings.csv'))
df_rankings_women = pd.read_csv(os.path.join(directory_path, 'ittf_rankings_women.csv'))

# Analyzing gender distribution
gender_distribution = df_player_info['Gender'].value_counts()

# Analyzing top countries representation in rankings
top_countries_men = df_rankings['Assoc'].value_counts().head(10)
top_countries_women = df_rankings_women['Assoc'].value_counts().head(10)

# Analyzing trends over time for both men and women
avg_points_per_year_men = df_rankings.groupby('YearNum')['Points'].mean().reset_index()
avg_points_per_year_women = df_rankings_women.groupby('YearNum')['Points'].mean().reset_index()

# Visualizing the trends
plt.figure(figsize=(12, 6))
plt.plot(avg_points_per_year_men['YearNum'], avg_points_per_year_men['Points'], label='Men', marker='o')
plt.plot(avg_points_per_year_women['YearNum'], avg_points_per_year_women['Points'], label='Women', marker='x')
plt.title('Average Ranking Points Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Points')
plt.legend()
plt.grid(True)
plt.show()