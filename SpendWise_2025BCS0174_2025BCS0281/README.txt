SpendWise - Personal Expense Analyzer
K Thanayan Reddy (2025BCS0174), Pratik Raj (2025BCS0281), IIIT Kottayam

Files:
  SpendWise.ipynb      main notebook (already executed, outputs saved)
  spendwise.py         helper functions used by the notebook
  generate_data.py     creates data/expenses.csv (seed 42)
  data/expenses.csv    synthetic expenses Jan-Jun 2026
  charts/              saved charts
  spendwise.db         SQLite database (table: transactions)
  summary_report.txt, summary.csv, overspending.csv   generated summary
  Report_SpendWise.pdf project report

How to run:
  pip install pandas matplotlib jupyter
  python generate_data.py
  jupyter notebook SpendWise.ipynb
