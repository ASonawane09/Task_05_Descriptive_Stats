import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Load dataset
file_path = 'syracuse_mbb_2023_24_stats.csv'
df = pd.read_csv(file_path)

sns.set(style="whitegrid")

# 1. Points by Player
plt.figure(figsize=(12,6))
sns.barplot(x='Player', y='PTS', data=df.sort_values('PTS', ascending=False))
plt.title('Total Points Scored by Player (2023-24 Season)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Points')
plt.xlabel('Player')
plt.tight_layout()
plt.savefig('images/points_by_player.png', dpi=300, bbox_inches='tight')
plt.clf()

# 2. Rebounds by Player
plt.figure(figsize=(12,6))
sns.barplot(x='Player', y='TOT', data=df.sort_values('TOT', ascending=False))
plt.title('Total Rebounds by Player (2023-24 Season)')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Total Rebounds')
plt.xlabel('Player')
plt.tight_layout()
plt.savefig('images/rebounds_by_player.png', dpi=300, bbox_inches='tight')
plt.clf()

# 3. FG% vs Points
plt.figure(figsize=(10,6))
sns.scatterplot(x='FG%', y='PTS', data=df, hue='Player', s=100)
plt.title('Field Goal Percentage vs. Points Scored')
plt.xlabel('Field Goal Percentage')
plt.ylabel('Points Scored')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('images/fg_percent_vs_points.png', dpi=300, bbox_inches='tight')
plt.clf()

# 4. Defensive Contribution
df['Defense_Score'] = df['BLK'] + df['STL']
plt.figure(figsize=(12,6))
sns.barplot(x='Player', y='Defense_Score', data=df.sort_values('Defense_Score', ascending=False))
plt.title('Combined Blocks and Steals by Player')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Blocks + Steals')
plt.xlabel('Player')
plt.tight_layout()
plt.savefig('images/defense_score.png', dpi=300, bbox_inches='tight')
plt.clf()
