# Use Python 3.11-slim as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the project files from your host to the container
COPY ./src /app/src
COPY ./data /app/data
COPY ./tests /app/tests
COPY ./pipeline /app/pipeline
COPY pyproject.toml poetry.lock /app/

# Configure Poetry:
# - Disable virtualenv creation
# - Install dependencies (excluding the project itself)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Grant execution rights to the pipeline script
RUN chmod +x /app/pipeline/run-pipeline.sh

# Set the command to run the pipeline script using Bash
CMD ["/bin/bash", "-c", "/app/pipeline/run-pipeline.sh"]