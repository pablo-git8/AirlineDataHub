# Imports
import pandas as pd
from pandas.testing import assert_frame_equal
from ..src.transforms import transform_data  # Adjust the import according to your script's name/location

def test_transform_data(tmp_path):
    # Create a sample DataFrame to mimic raw data
    sample_data = {
        'OpCo': ['Vueling+', None],
        'Subsidiary': [None, 'Sub2'],
        'Subsidiary Name': ['Sub1', None],
        'Aircraft type': [None, 'Type2'],
        'OpCo Name': ['Vueling+', 'Op2'],
        'Arrival Country Name': ['Country1?', 'Country2'],
        'Departure Country Name': ['Country3', 'Country!4'],
        'Date': ['2022-01-01', '2022-04-15']
    }
    raw_df = pd.DataFrame(sample_data)

    # Define expected DataFrame after transformation
    expected_data = {
        'OpCo_Code': ['Vueling', 'Op2'],
        'Subsidiary_Code': ['NS', 'Sub2'],
        'Subsidiary_Name': ['Sub1', 'No subsidiary'],
        'Aircraft_Type': ['Not specified', 'Type2'],
        'OpCo_Name': ['Vueling', 'Op2'],
        'Arrival_Country_Name': ['Country1', 'Country2'],
        'Departure_Country_Name': ['Country3', 'Country4'],
        'Date': pd.to_datetime(['2022-01-01', '2022-04-15']),
        'Year': [2022, 2022],
        'Quarter': [1, 2]
    }
    expected_df = pd.DataFrame(expected_data)

    # Save the sample DataFrame as a CSV file in the tmp_path
    raw_file_path = tmp_path / "data/raw/Sample_Data.csv"
    raw_file_path.parent.mkdir(parents=True)  # Ensure the directory exists
    raw_df.to_csv(raw_file_path, index=False)

    # Adjust transform_data function to accept input and output file paths for testing
    output_file_path = tmp_path / "data/processed/aig_data_processed.csv"
    transform_data(input_file=str(raw_file_path), output_file=str(output_file_path))  # Modify the function to accept file paths as arguments

    # Read the processed DataFrame from the output file
    result_df = pd.read_csv(output_file_path)

    # Assert that the result matches the expected DataFrame
    assert_frame_equal(result_df, expected_df, check_dtype=False)
