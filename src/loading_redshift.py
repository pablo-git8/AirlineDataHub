# Imports
import os
import boto3
import pandas as pd
import pandas as pd
from sqlalchemy import create_engine


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

# SQLite setup
sqlite_engine = create_engine('sqlite:///../data/processed/aig_datawarehouse.db')

# Read a table from SQLite, save it as CSV, and upload to S3
def upload_table_to_s3(table_name, sqlite_engine, s3_client, bucket_name, s3_folder):
    df = pd.read_sql_table(table_name, sqlite_engine)
    csv_file = f"{table_name}.csv"
    df.to_csv(csv_file, index=False)
    
    s3_path = f"{s3_folder}/{csv_file}"
    s3_client.upload_file(csv_file, bucket_name, s3_path)
    print(f"Uploaded {table_name} to s3://{bucket_name}/{s3_path}")

# AWS S3 and Redshift setup
S3_BUCKET_NAME = os.getenv("BUCKET_NAME")
S3_FOLDER = os.getenv("OBJECT_KEY")  # Path in S3 where CSV files will be stored

# Initialize a boto3 client
s3_client = boto3.client('s3')

# List of table names to transfer
table_names = ['Dim_OpCo', 'Dim_Airport', 'Dim_Time', 'Fact_Flights']

# Upload each table as a CSV to S3
for table_name in table_names:
    upload_table_to_s3(table_name, sqlite_engine, s3_client, S3_BUCKET_NAME, S3_FOLDER)

# Initialize Redshift Data client to execute SQL commands
redshift_data_client = boto3.client('redshift-data')

# Function to execute the COPY command for each table from S3 to Redshift
def copy_to_redshift(table_name, s3_folder, redshift_data_client, redshift_cluster_identifier, redshift_database, redshift_user):
    s3_path = f"s3://{S3_BUCKET_NAME}/{s3_folder}/{table_name}.csv"
    copy_command = f"""
    COPY {table_name}
    FROM '{s3_path}'
    IAM_ROLE 'arn:aws:iam::730335225805:role/RedshiftRole'
    CSV IGNOREHEADER 1;
    """
    response = redshift_data_client.execute_statement(
        ClusterIdentifier=redshift_cluster_identifier,
        Database=redshift_database,
        DbUser=redshift_user,
        Sql=copy_command
    )
    print(f"Started COPY command for {table_name}, ExecutionId: {response['Id']}")

REDSHIFT_CLUSTER_IDENTIFIER = os.getenv("REDSHIFT_CLUSTER_IDENTIFIER")
REDSHIFT_DATABASE = os.getenv("REDSHIFT_DATABASE")
REDSHIFT_USER = os.getenv("REDSHIFT_USER")

# Copy each table from S3 to Redshift
for table_name in table_names:
    copy_to_redshift(table_name, S3_FOLDER, redshift_data_client, REDSHIFT_CLUSTER_IDENTIFIER, REDSHIFT_DATABASE, REDSHIFT_USER)