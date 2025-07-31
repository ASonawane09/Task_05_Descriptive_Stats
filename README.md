# Task_05_Descriptive_Stats

## Overview

This project investigates the capabilities of Large Language Models (LLMs) in analyzing sports statistics through natural language queries. Using the Syracuse Men’s Basketball 2023-24 season dataset, I tested how accurately an LLM can answer descriptive and analytical questions about player and team performance.

---

## Dataset

The dataset includes stats for 13 players over 32 games with features such as points scored, rebounds, assists, shooting percentages, steals, and blocks.

---

## Methodology

1. **Data Preparation:**  
   Cleaned and structured the dataset for easy querying.

2. **Question Design:**  
   Developed 15 natural language questions ranging from basic facts to complex insights about team and player performance.

3. **LLM Interaction:**  
   Submitted questions to an LLM with dataset context and recorded responses.

4. **Validation:**  
   Wrote Python scripts to validate LLM answers using direct calculations on the dataset.

5. **Visualization:**  
   Created charts visualizing key statistics to aid interpretation and reporting.

---

## Visualizations

### Points by Player  
![Points by Player](images/points_by_player.png)

### Rebounds by Player  
![Rebounds by Player](images/rebounds_by_player.png)

### Field Goal Percentage vs. Points  
![FG% vs Points](images/fg_percent_vs_points.png)

### Defensive Contributions (Blocks + Steals)  
![Defense Score](images/defense_score.png)

---

## Usage

- Run the validation script `scripts/validate_llm_answers.py` to replicate data validations.  
- Use `scripts/visualize_stats.py` to regenerate the visualizations.  
- Review `prompts/questions_and_answers.md` for all LLM interaction prompts and responses.

---

## Contact

For questions or feedback, please contact: Aakanksha Sonawane - assonawa@syr.edu

---

*Note: Dataset file is not included in this repository due to size and privacy considerations.*

