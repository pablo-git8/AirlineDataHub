# Imports
import pandas as pd
import sqlite3
from ..src.loading_sqlite import load_data_to_sqlite  # Adjust the import according to your script's name/location

def test_load_data_to_sqlite(monkeypatch, tmp_path):
    # Sample data that mimics the processed CSV data
    sample_data = {
        'OpCo_Code': ['Op1', 'Op2'],
        'OpCo_Name': ['OpName1', 'OpName2'],
        'Subsidiary_Code': ['Sub1', 'Sub2'],
        'Subsidiary_Name': ['SubName1', 'SubName2'],
        'Departure_Airport_Code': ['Dep1', 'Dep2'],
        'Departure_Airport_Name': ['DepName1', 'DepName2'],
        'Departure_Country_Code': ['DepCountry1', 'DepCountry2'],
        'Departure_Country_Name': ['DepCountryName1', 'DepCountryName2'],
        'Departure_Region': ['DepRegion1', 'DepRegion2'],
        'Arrival_Airport_Code': ['Arr1', 'Arr2'],
        'Arrival_Airport_Name': ['ArrName1', 'ArrName2'],
        'Arrival_Country_Code': ['ArrCountry1', 'ArrCountry2'],
        'Arrival_Country_Name': ['ArrCountryName1', 'ArrCountryName2'],
        'Arrival_Region': ['ArrRegion1', 'ArrRegion2'],
        'Aircraft_Type': ['Type1', 'Type2'],
        'Passengers': [100, 150],
        'Flights': [1, 2],
        'Date': ['2022-01-01', '2022-04-15'],
        'Year': [2022, 2022],
        'Quarter': [1, 2]
    }
    df = pd.DataFrame(sample_data)

    # Mock pd.read_csv to return the sample DataFrame instead of reading from a file
    monkeypatch.setattr(pd, "read_csv", lambda *args, **kwargs: df)

    # Use an in-memory SQLite database for testing
    with sqlite3.connect(':memory:') as conn:
        # Mock the connection to use the in-memory SQLite database
        monkeypatch.setattr("sqlite3.connect", lambda *args, **kwargs: conn)

        # Call the function to test
        load_data_to_sqlite()

        # Assert conditions to verify the database state
        for table in ['Dim_OpCo', 'Dim_Airport', 'Dim_Time', 'Fact_Flights']:
            cursor = conn.cursor()
            cursor.execute(f'SELECT COUNT(*) FROM {table}')
            count = cursor.fetchone()[0]
            assert count > 0  # Assert that rows were inserted into each table
