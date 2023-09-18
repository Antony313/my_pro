# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install mongoengine

# Make port 8083 available to the world outside this container
EXPOSE 8083  

# Define environment variable
ENV NAME World

# Run your Flask app when the container launches
CMD ["python", "main.py"]
