# This is a first version of Dockerfile without Multistage build
# Use an official Python runtime as the base image  
#FROM python:3.9-slim  
# Set the working directory inside the container  
#WORKDIR /app  
# Copy the requirements file into the container  
#COPY requirements.txt .  
# Install the app's dependencies  
#RUN pip install --no-cache-dir -r requirements.txt  
# Copy the rest of the app's code into the container  
#COPY . .  
# Expose the port the app runs on (matches Flask's port=5000)  
#EXPOSE 5000  
# Command to run the app when the container starts  
#CMD ["python", "app.py"] 

# Second version with Multistage build
# Stage 1: Build dependencies  
FROM python:3.9-slim AS builder  
WORKDIR /app  
	COPY requirements.txt .  
	RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt  
 
# Stage 2: Run the app with a minimal image  
FROM python:3.9-slim  
WORKDIR /app  
COPY --from=builder /app/wheels /wheels  
RUN pip install --no-cache /wheels/*  
COPY . .  
EXPOSE 5000  
CMD ["python", "app.py"]  


