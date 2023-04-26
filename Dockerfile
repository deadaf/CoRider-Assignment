# Base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .
COPY .env .
# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port used by the application
EXPOSE 8001

# Start the application
CMD ["python3","app.py"]