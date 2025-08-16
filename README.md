# Task_05_Descriptive_Stats

## Overview
This project investigates the capabilities of Large Language Models (LLMs) in analyzing sports statistics through natural language queries. Using the Syracuse Men’s Basketball 2023–24 season dataset, the study evaluates how accurately an LLM can answer both descriptive (Phase 1) and advanced reasoning (Phase 2) questions about player and team performance.

---

## Dataset
The dataset contains statistics for 13 players over 32 games, including:
- Points scored
- Rebounds
- Assists
- Shooting percentages (FG%, 3P%, FT%)
- Steals
- Blocks

---

## Methodology

### Phase 1 – Descriptive Analysis
**Data Preparation**
- Cleaned and structured the dataset for easy querying.
- Handled missing values and ensured column naming consistency.

**Question Design**
- Developed 15 natural language questions ranging from basic counts to moderately complex queries.

**LLM Interaction**
- Provided dataset context to an LLM and recorded responses for each question.

**Validation**
- Wrote Python scripts to validate LLM answers via direct calculations on the dataset.

**Visualization**
- Created bar charts, scatter plots, and composite metrics to visualize results.

---

### Phase 2 – Advanced Reasoning (No Code)
This phase moved beyond surface-level stats into multi-step reasoning, requiring the LLM to connect multiple data points, aggregate information, and justify conclusions.

**Types of Questions Asked**
1. **Composite Metrics Analysis** – Normalized multiple stats and combined them into weighted scores to find top performers.
2. **Contextual Performance** – Evaluated player impact in specific game conditions (e.g., team scoring under 70 points).
3. **Conditional Leaders** – Applied thresholds (e.g., minutes played) combined with ratio-based metrics.
4. **Impact on Win/Loss** – Identified stats most correlated with winning outcomes.

**Evaluation Approach**
- **Prompt Design for Reasoning** – Structured questions to encourage step-by-step logic.
- **Accuracy Verification** – Python scripts replicated all calculations.
- **Reasoning Traceability** – Reviewed explanations for clarity of intermediate steps.
- **Error Categorization** – Classified mistakes into computation, filtering, or misinterpretation.

---

## Key Advanced Insights
- **Strategic Priorities**: Improve defensive rebounding, reduce live-ball turnovers, and reallocate 3PT attempts to high-efficiency shooters (notably Chris Bell).
- **Player Development Focus**: Judah Mintz for offensive leadership and late-game execution; Maliq Brown as the defensive anchor.
- **Clutch Blueprint**: Empty-side pick-and-roll (Mintz–Brown) with Spain PnR counters.
- **Turnover Reduction**: Codified press-break roles and added late-clock ATO sets.
- **Rebounding Plan**: Wings crash from weak-side, Brown anchors, guards secure inside position.
- **Fast-Break Identity**: Mintz leads, Copeland as secondary engine, disciplined lane fills.
- **Matchup Adjustments**: Tailored PnR approaches vs. drop coverage and switch-everything defenses.
- **Foul Management**: Early rotation strategy for Brown to avoid foul trouble.
- **Bench Roles**: Situational deployment for Copeland, Williams, McLeod, Cuffe, and Taylor.
- **KPI Tracking**: Possession control, shot allocation, advantage creation, and late-game FT%.

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
