# Use official Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY main.py .

# Expose Prometheus metrics port
EXPOSE 8000

# Run the app
CMD ["python", "main.py"]

