# Imports
import pandas as pd
import sqlite3

def load_data_to_sqlite():
    # Load processed dataframe
    aig_df = pd.read_csv('../data/processed/aig_data_processed.csv')

    # Insert data into Dim_OpCo table
    def insert_dim_opco(conn, row):
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT OR IGNORE INTO Dim_OpCo (OpCo_Code, OpCo_Name, Subsidiary_Code, Subsidiary_Name)
                            VALUES (?, ?, ?, ?)''',
                           (row['OpCo_Code'], row['OpCo_Name'], row['Subsidiary_Code'], row['Subsidiary_Name']))
            cursor.execute('SELECT OpCo_ID FROM Dim_OpCo WHERE OpCo_Code = ?', (row['OpCo_Code'],))
            return cursor.fetchone()[0]
        finally:
            cursor.close()

    # Insert data into Dim_Airport table
    def insert_dim_airport(conn, row, airport_code, airport_name, country_code, country_name, region):
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT OR IGNORE INTO Dim_Airport (Airport_Code, Airport_Name, Country_Code, Country_Name, Region)
                            VALUES (?, ?, ?, ?, ?)''',
                           (row[airport_code], row[airport_name], row[country_code], row[country_name], row[region]))
            cursor.execute('SELECT Airport_ID FROM Dim_Airport WHERE Airport_Code = ?', (row[airport_code],))
            return cursor.fetchone()[0]
        finally:
            cursor.close()

    # Insert data into Dim_Time table
    def insert_dim_time(conn, row):
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT OR IGNORE INTO Dim_Time (Date, Year, Quarter)
                            VALUES (?, ?, ?)''',
                           (row['Date'], row['Year'], row['Quarter']))
            cursor.execute('SELECT Time_ID FROM Dim_Time WHERE Date = ?', (row['Date'],))
            return cursor.fetchone()[0]
        finally:
            cursor.close()

    # Insert data into Fact_Flights table
    def insert_fact_flights(conn, row, opco_id, departure_airport_id, arrival_airport_id, time_id):
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO Fact_Flights (OpCo_ID, Departure_Airport_ID, Arrival_Airport_ID, Time_ID, Aircraft_Type, Passengers, Flights)
                            VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (opco_id, departure_airport_id, arrival_airport_id, time_id, row['Aircraft_Type'], row['Passengers'], row['Flights']))
        finally:
            cursor.close()

    # Connect to the SQLite database
    with sqlite3.connect('../data/processed/aig_data_warehouse.db') as conn:
        cursor = conn.cursor()

        # Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dim_OpCo (
            OpCo_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OpCo_Code TEXT UNIQUE,
            OpCo_Name TEXT,
            Subsidiary_Code TEXT,
            Subsidiary_Name TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dim_Airport (
            Airport_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Airport_Code TEXT UNIQUE,
            Airport_Name TEXT,
            Country_Code TEXT,
            Country_Name TEXT,
            Region TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dim_Time (
            Time_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Date DATE UNIQUE,
            Year INTEGER,
            Quarter INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Fact_Flights (
            Flight_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OpCo_ID INTEGER,
            Departure_Airport_ID INTEGER,
            Arrival_Airport_ID INTEGER,
            Time_ID INTEGER,
            Aircraft_Type TEXT,
            Passengers INTEGER,
            Flights INTEGER,
            FOREIGN KEY (OpCo_ID) REFERENCES Dim_OpCo(OpCo_ID),
            FOREIGN KEY (Departure_Airport_ID) REFERENCES Dim_Airport(Airport_ID),
            FOREIGN KEY (Arrival_Airport_ID) REFERENCES Dim_Airport(Airport_ID),
            FOREIGN KEY (Time_ID) REFERENCES Dim_Time(Time_ID)
        )
        ''')

        # Commit the changes to create tables
        conn.commit()

        # Iterate over the DataFrame rows and use the insertion functions to populate the database
        try:
            for _, row in aig_df.iterrows():
                opco_id = insert_dim_opco(conn, row)
                departure_airport_id = insert_dim_airport(conn, row, 'Departure_Airport_Code', 'Departure_Airport_Name', 'Departure_Country_Code', 'Departure_Country_Name', 'Departure_Region')
                arrival_airport_id = insert_dim_airport(conn, row, 'Arrival_Airport_Code', 'Arrival_Airport_Name', 'Arrival_Country_Code', 'Arrival_Country_Name', 'Arrival_Region')
                time_id = insert_dim_time(conn, row)
                insert_fact_flights(conn, row, opco_id, departure_airport_id, arrival_airport_id, time_id)
        except Exception as e:  # Catching a broad exception
            print(f"An error occurred during general data insertion: {e}")
            conn.rollback()  # Rollback any changes if part of the operations failed
        else:
            conn.commit()  # Commit the transaction if all operations succeeded

if __name__ == '__main__':
    load_data_to_sqlite()
