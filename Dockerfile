FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt to working directory
COPY requirements.txt .

# Install Python requirements (pandas)
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python script to working directory
COPY src/clean_orders.py .

# Call script when starting the container
CMD ["python", "clean_orders.py"]