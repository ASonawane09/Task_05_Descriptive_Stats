import pandas as pd

# Load dataset
file_path = 'syracuse_mbb_2023_24_stats.csv'  # update path as needed
df = pd.read_csv(file_path)

# 1. How many games did the team play this season?
team_games_played = df['GP'].max()

# 2. Who scored the most points this season?
top_scorer = df.loc[df['PTS'].idxmax()]['Player']
top_points = df['PTS'].max()

# 3. Which player had the highest field goal percentage?
top_fg_player = df.loc[df['FG%'].idxmax()]['Player']
top_fg_percent = df['FG%'].max()

# 4. Who played the most minutes?
top_minutes_player = df.loc[df['MIN'].idxmax()]['Player']
top_minutes = df['MIN'].max()

# 5. Who had the most rebounds this season?
top_rebounder = df.loc[df['TOT'].idxmax()]['Player']
top_rebounds = df['TOT'].max()

# 6. Who had the highest free throw percentage?
top_ft_player = df.loc[df['FT%'].idxmax()]['Player']
top_ft_percent = df['FT%'].max()

# 7. What was the team’s average points per game?
team_avg_pts_per_game = df['PTS'].sum() / team_games_played

# 8. Which player had the highest average assists per game?
df['AST_per_game'] = df['AST'] / df['GP']
top_ast_player = df.loc[df['AST_per_game'].idxmax()]['Player']
top_ast_avg = df['AST_per_game'].max()

# 9. Which player had the best defensive performance based on blocks and steals combined?
df['Defense_Score'] = df['BLK'] + df['STL']
best_defender = df.loc[df['Defense_Score'].idxmax()]['Player']
best_defense_score = df['Defense_Score'].max()

# 10. What is the average number of turnovers per game for the team?
team_avg_turnovers_per_game = df['TO'].sum() / team_games_played

# 11. Who contributed most to the team’s offense (points + assists)?
df['Offense_Score'] = df['PTS'] + df['AST']
top_offensive_player = df.loc[df['Offense_Score'].idxmax()]['Player']
top_offense_score = df['Offense_Score'].max()

# 12. Who contributed most to the team’s defense (rebounds + steals + blocks)?
df['Defense_Total'] = df['TOT'] + df['STL'] + df['BLK']
top_defensive_player = df.loc[df['Defense_Total'].idxmax()]['Player']
top_defense_total = df['Defense_Total'].max()

# 13. Which player had the best scoring efficiency (points per shot attempted)?
df['Shots_Attempted'] = df['FGA'] + df['FTA']
df['Scoring_Efficiency'] = df['PTS'] / df['Shots_Attempted']
best_scorer_efficiency_player = df.loc[df['Scoring_Efficiency'].idxmax()]['Player']
best_scorer_efficiency = df['Scoring_Efficiency'].max()

# 14. If the coach wants to improve scoring, which player should they focus on?
# Using points + assists as proxy
coach_focus_player = top_offensive_player

# 15. Who had the best all-around performance combining offense and defense metrics?
df['All_Around_Score'] = df['Offense_Score'] + df['Defense_Total']
best_all_around_player = df.loc[df['All_Around_Score'].idxmax()]['Player']
best_all_around_score = df['All_Around_Score'].max()

# Print all answers
print(f"1. Team games played: {team_games_played}")
print(f"2. Top scorer: {top_scorer} ({top_points} points)")
print(f"3. Highest FG%: {top_fg_player} ({top_fg_percent:.3f})")
print(f"4. Most minutes played: {top_minutes_player} ({top_minutes} minutes)")
print(f"5. Most rebounds: {top_rebounder} ({top_rebounds} rebounds)")
print(f"6. Highest FT%: {top_ft_player} ({top_ft_percent:.3f})")
print(f"7. Team average points per game: {team_avg_pts_per_game:.2f}")
print(f"8. Highest assists per game: {top_ast_player} ({top_ast_avg:.2f} assists/game)")
print(f"9. Best defensive player (blocks + steals): {best_defender} ({best_defense_score} total)")
print(f"10. Team average turnovers per game: {team_avg_turnovers_per_game:.2f}")
print(f"11. Top offensive contributor (points + assists): {top_offensive_player} ({top_offense_score})")
print(f"12. Top defensive contributor (rebounds + steals + blocks): {top_defensive_player} ({top_defense_total})")
print(f"13. Best scoring efficiency (points per shot attempted): {best_scorer_efficiency_player} ({best_scorer_efficiency:.3f})")
print(f"14. Coach should focus on: {coach_focus_player}")
print(f"15. Best all-around player (offense + defense): {best_all_around_player} ({best_all_around_score})")
