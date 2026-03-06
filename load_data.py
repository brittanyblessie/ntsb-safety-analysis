"""
load_data.py

Initial data exploration of the NTSB aviation accident database.
Connects to the Access database, loads the events table, and prints
basic information about the dataset including shape and column names.

Author: Brittany Blessie
Data source: NTSB Aviation Accident Database (1982-2024)
"""

import pyodbc
import pandas as pd

# Path to the NTSB Access database file
db_path = r"C:\Users\brittany.blessie\Downloads\avall\avall.mdb"

# Connection string for Microsoft Access driver
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"Dbq=" + db_path + ";"
)

# Establish database connection
conn = pyodbc.connect(conn_str)

# Load the main events table
df = pd.read_sql("SELECT * FROM events", conn)

# Print basic dataset information for exploration
print(df.shape)
print(df.columns.tolist())
