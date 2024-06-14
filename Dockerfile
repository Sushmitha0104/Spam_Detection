# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the model file exists and is not empty
RUN test -s /app/spam_classifier.joblib || (echo "Model file is missing or empty!" && exit 1)

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME SpamDetection

# Run app.py when the container launches
CMD ["python", "app.py"]
