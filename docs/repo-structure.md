AirTrafficInsights/
├── data/                       # Data folder for raw and processed datasets
│   ├── raw/                    # Raw data files, e.g., CSV files from S3 (optional, for future needs)
│   └── processed/              # Processed data files, post-cleaning (optional, for future needs)
│   └──country_code_map.json    # Helper file for validation tests (country code mapping)
│
├── sql/                        # SQL queries used in general
│   ├── schema_create.sql       # Queries for schema creation
│   └── table_population.sql    # Queries for data insertion into DDBB
│
├── src/                        # Source code for the project
│   ├── __init__.py             # src: Python module
│   ├── ingest.py               # Script for ingesting data from S3
│   └── clean_load.py           # Script for cleaning data and loading into Redshift
│
├── notebooks/                  # Jupyter notebooks for EDA and prototyping
│   └── data_exploration.ipynb  # EDA
│
├── tests/                      # Unit testing cases for the project
│   ├── __init__.py             # test: Python module
│   ├── test_ingest.py          # Testing test_ingest script
│   └── test_clean_load.py      # Testing test_clean_load script
│
├── docs/                       # Documentation for the project
│   ├── ER_diagram.png          # ER diagram for the data model
│   └── project_overview.md     # Overview and documentation of the project
│   └── repo_structure.md       # Repository structure
│
├── docker/                     # Folder for future needs of more Dockerfiles
│   └── Dockerfile              # Dockerfile for easy deployment and reproducibility
│
├── .env.example                # Example environment variables file (.env is gitignored)
├── pyproject.toml              # Poetry dependency file
├── poetry.lock                 # Lock file to ensure consistent installs
├── docker-compose.yaml         # Docker compose file for easy building
├── .dockerignore               # Files to ignore when building Docker images 
├── .ruff.toml                  # Configuration file for Ruff linter
├── .gitignore                  # Standard gitignore file
└── README.md                   # Project README with an overview, setup, and usage instructions