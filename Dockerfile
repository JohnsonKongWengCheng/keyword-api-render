# Dockerfile — use python 3.10
FROM python:3.10-slim

# Install system deps for building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libffi-dev libssl-dev wget git \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Expose and run
ENV PORT=8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
