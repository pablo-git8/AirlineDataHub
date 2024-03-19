# Imports
import os
import boto3
import pandas as pd
from io import StringIO

def load_env_variables(env_file='../.env'):
    """Load variables from .env file, ignoring lines without '='."""
    with open(env_file, 'r') as file:
        for line in file:
            # Skip lines without an equals sign or comments
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

def ingest_data():
    """Ingest data from S3 and save it as a CSV."""
    # Load environment variables
    load_env_variables()

    # Create an S3 client
    s3 = boto3.client('s3')

    # Specify path to your file within the S3 bucket
    BUCKET_NAME = os.getenv('BUCKET_NAME')
    OBJECT_KEY = os.getenv('OBJECT_KEY')

    # Get the object from S3
    csv_obj = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)

    # Get the body of the object (the file content)
    body = csv_obj['Body']

    # Read the body into a string
    csv_string = body.read().decode('utf-8')

    # Use pandas to read the CSV string into a DataFrame
    aig_df = pd.read_csv(StringIO(csv_string))

    # Save the DataFrame to a CSV file
    aig_df.to_csv('../data/raw/Sample_Data.csv', index=False)

if __name__ == "__main__":
    ingest_data()
