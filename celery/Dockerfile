# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables for Celery (optional)
ENV C_FORCE_ROOT="true"

# Default command
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]

