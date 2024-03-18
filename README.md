# AirlineDataHub

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![bash](https://img.shields.io/badge/bash-4EAA25?style=for-the-badge&logo=gnu%20bash&logoColor=white)
![docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![docker-compose](https://img.shields.io/badge/docker%20compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![aws-s3](https://img.shields.io/badge/aws%20s3-569A31?style=for-the-badge&logo=amazon%20s3&logoColor=white)
![aws-redshift](https://img.shields.io/badge/aws%20redshift-EE0000?style=for-the-badge&logo=amazon%20aws&logoColor=white)

## Overview
`AirlineDataHub` is a comprehensive data engineering solution designed to simplify the analysis and warehousing of aviation data. By leveraging the power of Python for data extraction and cleaning, SQL for data storage and manipulation, and AWS services for scalable data storage and analytics, this repository provides a robust foundation for data handling in the aviation sector.

From ingesting CSV files from AWS S3 buckets, running ETL pipelines to performing exploratory data analysis (EDA) and loading processed data into AWS Redshift for advanced analytics, `AirlineDataHub` encapsulates best practices in data engineering to facilitate insightful aviation data analysis.

## Repository Structure
For a detailed explanation of the repository structure, please refer to the [Repository Structure Documentation](docs/repo_structure.md).

## Setup Instructions
1. **Clone the Repository:**
   ```
   git clone https://github.com/pablo-git8/AirlineDataHub.git
   cd AirlineDataHub
   ```

2. **Environment Setup:**
   - Ensure Python and Poetry are installed on your system.
   - Install project dependencies using Poetry:
     ```
     poetry install
     ```

3. **AWS S3 and Redshift Configuration:**
   - Configure your AWS CLI with the necessary access credentials.
   - Ensure there is an existent S3 bucket with the data
   - Ensure your AWS Redshift cluster is set up and accessible.

4. **Environment Variables:**
   - Copy the `.env.example` file to `.env` and update it with your actual configuration details.

5. **Docker (Optional):**
   - If you prefer to use Docker, ensure Docker and Docker Compose are installed.
   - Build and run your containers (this will run the full pipeline):
     ```
     docker-compose up --build
     ```

## Usage
- **Running the Pipeline:**
  To execute the full data pipeline, navigate to the `pipeline` directory and run:
  ```
  ./run-pipeline.sh
  ```

- **Exploratory Data Analysis (EDA):**
  Launch Jupyter Notebooks for checking the development processes, data exploration and prototyping:
  ```
  jupyter notebook notebooks/data_exploration.ipynb
  jupyter notebook notebooks/data_transformation.ipynb
  jupyter notebook notebooks/data_modeling.ipynb
  ```
  These files provide the ground basis for script development for the pipeline. Have a look at the scripts here:
  ```
  ../src/ingestion.py        # Loads raw data from S3 and saves a raw copy
  ../src/transforms.py       # Perform all necessary transformation and saves a cleaned copy
  ../src/loading-sqlite.py   # Data modeling. Creates transitory DDBB for later copy to a Data Warehouse
  ../src/loading-redshift.py # Loads the data to AWS Redshift
  ```
  Additionally the following script creates an aggregated table optimized for showing the number of passengers by `OpCo`, `Country`, `Region`, `Year`, `Quarter of the year (Q1, Q2, Q3 or Q4)`:
  ```
  ../src/create_agg_table.py # Creates aggregated table into SQL DDBB
  ```

- **Testing:**
  Run unit tests to ensure reliability:
  ```
  poetry run pytest tests/
  ```

## Documentation
For more detailed information about the project overview, data model, and specific components, refer to the `docs` directory.

- **ER Diagram and Database Schema**: Visual representations of the data model and database schema are available in `ER_diagram.jpg` and `db_schema.pdf`, respectively.

- **Project Overview**: For a comprehensive overview of the project, including its goals, methodologies, and technologies used, check out `project_overview.md`.

## License
`AirlineDataHub` is released under the [MIT License](LICENSE).

## Contact
For any queries or further assistance, please contact [Pablo Ruiz Lopez](pablo.devdt@gmail.com).