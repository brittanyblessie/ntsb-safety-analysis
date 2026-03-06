"""
phase_of_flight.py

Analyzes the top 10 accident types by occurrence across all US civil
aviation accidents using the NTSB Events_Sequence table. Results are
visualized as a horizontal bar chart.

Author: Brittany Blessie
Data source: NTSB Aviation Accident Database (1982-2024)
"""

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Path to the NTSB Access database file
db_path = r"C:\Users\brittany.blessie\Downloads\avall\avall.mdb"

# Connection string for Microsoft Access driver
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"Dbq=" + db_path + ";"
)

# Establish database connection
conn = pyodbc.connect(conn_str)

# Load the events sequence table
df = pd.read_sql("SELECT * FROM Events_Sequence", conn)

# Count top 10 accident types by occurrence
phase_counts = df['Occurrence_Description'].value_counts().head(10)

# Plot top 10 accident types
plt.figure(figsize=(12, 7))
bars = plt.barh(range(len(phase_counts)), phase_counts.values, color='steelblue')
plt.yticks(range(len(phase_counts)), phase_counts.index, fontsize=9)
plt.title('Top 10 Accident Types by Occurrence', fontsize=14, pad=15)
plt.xlabel('Number of Accidents', fontsize=11)
plt.gca().invert_yaxis()
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('phase_of_flight.png', dpi=150)
plt.show()
```
