#!/bin/bash

# Navigate to the src directory where Python scripts are located
cd ../src/

# Ensure scripts are executable
chmod +x ingestion.py transforms.py loading-sqlite.py

# Run the Python scripts in order
python ingestion.py
python transforms.py
python loading-sqlite.py
python loading-redshift.py

# Return to the original directory
cd -
