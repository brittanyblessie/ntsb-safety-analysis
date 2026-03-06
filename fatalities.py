"""
fatalities.py

Analyzes US civil aviation fatality trends by year using the NTSB
accident database. Fatality counts are derived from the injury table
and merged with event data to show year over year trends.

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

# Load injury and events tables
injury = pd.read_sql("SELECT * FROM injury", conn)
events = pd.read_sql("SELECT ev_id, ev_year FROM events", conn)

# Filter to fatal injuries only
fatalities = injury[injury['injury_level'] == 'FATL']

# Merge fatalities with event year data
merged = fatalities.merge(events, on='ev_id')

# Remove incomplete current year data
merged = merged[merged['ev_year'] < 2025]

# Sum total fatalities per year
fatalities_by_year = merged.groupby('ev_year')['inj_person_count'].sum()

# Plot fatalities by year
plt.figure(figsize=(14, 6))
plt.bar(fatalities_by_year.index, fatalities_by_year.values, color='steelblue', width=0.7)
plt.title('US Aviation Fatalities by Year', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=11)
plt.ylabel('Number of Fatalities', fontsize=11)
plt.xticks(fatalities_by_year.index, rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('fatalities_by_year.png', dpi=150)
plt.show()