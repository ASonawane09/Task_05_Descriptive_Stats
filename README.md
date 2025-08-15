# Task_05_Descriptive_Stats

## Overview
This project investigates the capabilities of Large Language Models (LLMs) in analyzing sports statistics through natural language queries. Using the Syracuse Men’s Basketball 2023–24 season dataset, the study evaluates how accurately an LLM can answer both **descriptive** (Phase 1) and **advanced reasoning** (Phase 2) questions about player and team performance.

## Dataset
The dataset contains statistics for **13 players** over **32 games**, including:
- Points scored  
- Rebounds  
- Assists  
- Shooting percentages (FG%, 3P%, FT%)  
- Steals  
- Blocks  

## Methodology

### Phase 1 – Descriptive Analysis
**Data Preparation**
- Cleaned and structured the dataset for easy querying.  
- Handled missing values and ensured column naming consistency.  

**Question Design**
- Developed **15 natural language questions** from basic counts to moderately complex queries.  

**LLM Interaction**
- Provided dataset context to an LLM and recorded responses for each question.  

**Validation**
- Wrote Python scripts to validate LLM answers via direct calculations on the dataset.  

**Visualization**
- Created bar charts, scatter plots, and composite metrics to visualize results.  

---

### Phase 2 – Advanced Reasoning
This phase moved beyond surface-level stats into **multi-step reasoning** where the LLM had to connect multiple data points, aggregate information, and justify conclusions.

**Types of Questions Asked**
- **Composite Metrics Analysis** – e.g., “Which player had the highest combined efficiency when considering points, rebounds, assists, and shooting percentage?”  
  - Required the LLM to normalize different metrics and combine them into a weighted score.
- **Contextual Performance** – e.g., “Who contributed the most in games where the team scored under 70 points?”  
  - Involved filtering games by a condition, then calculating player impact.
- **Conditional Leaders** – e.g., “Among players with more than 20 minutes per game, who had the highest steal-to-turnover ratio?”  
  - Combined minutes played thresholds with a ratio-based metric.
- **Impact on Win/Loss** – e.g., “Which stat was most strongly associated with winning games?”  
  - Required correlation reasoning between game outcomes and multiple performance metrics.

**Evaluation Approach**
1. **Prompt Design for Reasoning**  
   - Each question was framed to force step-by-step logical reasoning.  
   - Prompts encouraged the model to explain *how* it arrived at the answer.
2. **Accuracy Verification**  
   - Python scripts replicated all calculations to confirm correctness.
3. **Reasoning Traceability**  
   - Responses were reviewed to see if the LLM explained intermediate steps clearly.
4. **Error Categorization**  
   - Wrong answers were classified into “computation errors”, “filtering mistakes”, or “misinterpretation of question intent”.

**Findings**
- LLMs performed **well** when the reasoning path was short and metrics were straightforward.  
- Performance dropped when:
  - Multiple filters were applied before calculation.
  - Metrics needed normalization or weighting.
- Best results occurred when the LLM was explicitly prompted to list steps before answering.

---

## Visualizations
- **Points by Player** – Total points scored by each player.  
- **Rebounds by Player** – Total rebounds for each player.  
- **Field Goal % vs. Points** – Scoring efficiency vs. total points.  
- **Defensive Contributions** – Combined blocks and steals.  

---

## Usage
Run the validation script:  
```bash
python validate_llm_answers.py
