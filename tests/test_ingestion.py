# Imports
import os
import boto3
import pandas as pd
from moto import mock_s3
from ..src.ingestion import ingest_data

@mock_s3
def test_ingest_data(tmp_path):
    # Setup mock S3
    conn = boto3.resource('s3', region_name='us-east-1')
    conn.create_bucket(Bucket='my-test-bucket')
    object_key = 'test/Sample_Data.csv'
    csv_content = 'col1,col2\nval1,val2'  # Sample CSV content

    # Add test object to the mock S3 bucket
    conn.Object('my-test-bucket', object_key).put(Body=csv_content)

    # Mock environment variables
    os.environ['BUCKET_NAME'] = 'my-test-bucket'
    os.environ['OBJECT_KEY'] = object_key

    # Mock the file path to use tmp_path fixture from pytest
    data_path = tmp_path / "data/raw"
    data_path.mkdir(parents=True)
    output_file = data_path / "Sample_Data.csv"

    # Run the ingest_data function, which should read from the mocked S3
    ingest_data(env_file=None, output_file=str(output_file))  # Adjust the function signature as needed

    # Read the result and validate
    result_df = pd.read_csv(output_file)

    # Validate the contents of the DataFrame
    assert result_df.iloc[0]['col1'] == 'val1'
    assert result_df.iloc[0]['col2'] == 'val2'
