FROM python:3.11-slim

# Install system-level dependencies for a clean build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application and service folders
COPY ./app /code/app
COPY ./mcp_service /code/mcp_service

# Run the FastAPI app
# Note: The MCP Server script is spawned by the app, not Docker directly
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]