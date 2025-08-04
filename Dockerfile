# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy app.py from host to container
COPY app.py .

# Run the Python app
CMD ["python", "app.py"]
