# Specify the base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del build-deps

# Copy the rest of the application code to the container
COPY . .

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
