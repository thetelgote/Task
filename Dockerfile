# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python dependencies (ignore errors if empty)
RUN pip install -r requirements.txt || true

# Run the Python script
CMD ["python", "app.py"]
