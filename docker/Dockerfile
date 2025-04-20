FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only the pipeline and dataset folders for now
COPY ./pipeline /app/pipeline
COPY ./datasets /app/datasets

# Install dependencies
COPY ./docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "pipeline/ingestion.py"]
