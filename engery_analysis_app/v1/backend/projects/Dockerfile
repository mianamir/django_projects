# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files to working directory
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]