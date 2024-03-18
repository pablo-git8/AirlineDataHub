#!/bin/bash

# Navigate to the src directory where Python scripts are located
cd ../src/

# Ensure scripts are executable
chmod +x ingestion.py transforms.py loading_sqlite.py loading_redshift.py

# Run the Python scripts in order
python ingestion.py
python transforms.py
python loading_sqlite.py
python loading_redshift.py

# Return to the original directory
cd -
