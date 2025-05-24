import os
import pandas as pd
import sqlite3

# Configuration
csv_folder = './csv2'   # Update this to your folder
db_name = 'Monthly_Prescription_Drug_Plan_Formulary_and_Pharmacy_Network_Information.db'       # Name of the SQLite DB file

# Connect to (or create) SQLite database
conn = sqlite3.connect(db_name)

# Loop through all .csv files in the folder
for filename in os.listdir(csv_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(csv_folder, filename)
        table_name = os.path.splitext(filename)[0]  # Use filename (without .csv) as table name

        # Read the CSV with pipe delimiter
        df = pd.read_csv(file_path, delimiter='|', encoding='latin-1')

        # Write to SQLite (replace if table already exists)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f'Imported {filename} into table "{table_name}".')

# Close the connection
conn.close()
print(f'\nAll files have been imported into {db_name}.')
