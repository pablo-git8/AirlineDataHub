# Imports
import pandas as pd
import re

def transform_data():
    """Transform raw AIG data and save the processed DataFrame."""

    # Load raw dataframe
    aig_df = pd.read_csv('../data/raw/Sample_Data.csv')

    # Address missing values in specified columns
    aig_df['Subsidiary'] = aig_df['Subsidiary'].fillna('NS')
    aig_df['Subsidiary Name'] = aig_df['Subsidiary Name'].fillna('No subsidiary')
    aig_df['Aircraft type'] = aig_df['Aircraft type'].fillna('Not specified')

    # Replace specific string in 'OpCo Name' column
    aig_df['OpCo Name'] = aig_df['OpCo Name'].replace('Vueling+', 'Vueling')

    # Clean and standardize country names
    clean_country_names = lambda name: re.sub(r'[^a-zA-Z0-9\s\.,-]', '', name.strip()).title()

    # Apply the cleaning function
    aig_df['Arrival Country Name'] = aig_df['Arrival Country Name'].apply(clean_country_names)
    aig_df['Departure Country Name'] = aig_df['Departure Country Name'].apply(clean_country_names)

    # Convert 'Date' column to datetime objects
    aig_df['Date'] = pd.to_datetime(aig_df['Date'])

    # Rename columns
    aig_df.rename(columns={
        'OpCo': 'OpCo_Code',
        'OpCo Name': 'OpCo_Name',
        'Subsidiary': 'Subsidiary_Code',
        'Subsidiary Name': 'Subsidiary_Name',
        'Departure Airport': 'Departure_Airport_Code',
        'Departure Airport Name': 'Departure_Airport_Name',
        'Departure Country': 'Departure_Country_Code',
        'Departure Country Name': 'Departure_Country_Name',
        'Departure Region': 'Departure_Region',
        'Arrival Airport': 'Arrival_Airport_Code',
        'Arrival Airport Name': 'Arrival_Airport_Name',
        'Arrival Country': 'Arrival_Country_Code',
        'Arrival Country Name': 'Arrival_Country_Name',
        'Arrival Region': 'Arrival_Region',
        'Aircraft type': 'Aircraft_Type',
        '# Passengers': 'Passengers',
        '# Flights': 'Flights'
    }, inplace=True)

    # Extract 'Year' and 'Quarter' from 'Date'
    aig_df['Year'] = aig_df['Date'].dt.year
    aig_df['Quarter'] = aig_df['Date'].dt.quarter

    # Remove any duplicated rows based on all columns
    aig_df = aig_df.drop_duplicates()

    # Save the processed DataFrame to a CSV file
    aig_df.to_csv('../data/processed/aig_data_processed.csv', index=False)

if __name__ == "__main__":
    transform_data()
