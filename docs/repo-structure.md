AirTrafficInsights/
│
├── data/                           # Data folder for raw and processed datasets
│   ├── raw/                        # Raw data files, e.g., CSV files from S3 (optional, for future needs)
│   ├── processed/                  # Processed data files, post-cleaning (optional, for future needs)
│   └──country_code_map.json        # Helper file for validation tests (country code mapping)
│
├── docker/                         # Folder for future needs of more Dockerfiles
│   └── Dockerfile                  # Dockerfile for easy deployment and reproducibility
│
├── docs/                           # Documentation for the project
│   ├── ER_diagram.jpg              # ER diagram for the data model
│   ├── db_shcema.pdf               # Database documentation
│   ├── repo_structure.md           # Repository structure
│   └── project_overview.md         # Overview and documentation of the project
│
├── notebooks/                      # Jupyter notebooks for EDA and prototyping
│   ├── data_modeling.ipynb         # Data modeling - dev
│   ├── data_transformation.ipynb   # Transformation - dev
│   └── data_exploration.ipynb      # EDA
│
├── pipeline/                       # Pipelines to execute
│   └── run-pipeline.sh             # Run the full pipeline bash file
│
├── sql/                            # SQL queries used in general
│   ├── schema_create.sql           # Queries for schema creation
│   ├── aggregated_table.sql        # Query for aggregated table creation
│   ├── get_schemas.sql             # Query for getting schema
│   └── table_population.sql        # Queries for data insertion into DDBB
│
├── src/                            # Source code for the project
│   ├── __init__.py                 # src: Python module
│   ├── ingestion.py                # Script for ingesting data from S3
│   ├── create_agg_table.py         # Script for creating aggregation table
│   ├── loading_redshift.py         # Script for loading data into Redshift
│   ├── loading_sqlite.py           # Script for loading data into transitory SQLite DDBB
│   └── transforms.py               # Script for data transformations
│
├── tests/                          # Unit testing cases for the project
│   ├── __init__.py                 # test: Python module
│   ├── test_ingest.py              # Testing ingestion script
│   ├── test_ingest.py              # Testing transform script
│   ├── test_loading_sqlite.py      # Testing loading_sqlite script
│   └── test_loading_redshift.py    # Testing loading_redshift script
│
├── pipeline/                       # Pipelines to execute
│   └── run-pipeline.sh             # Run the full pipeline bash file
│
├── .env.example                    # Example environment variables file (.env is gitignored)
├── pyproject.toml                  # Poetry dependency file
├── poetry.lock                     # Lock file to ensure consistent installs
├── docker-compose.yaml             # Docker compose file for easy building
├── .dockerignore                   # Files to ignore when building Docker images 
├── .ruff.toml                      # Configuration file for Ruff linter
├── .gitignore                      # Standard gitignore file
├── LICENSE                         # MIT License file
└── README.md                       # Project README with an overview, setup, and usage instructions