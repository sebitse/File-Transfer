# Use Python image
FROM python:3.12

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Set environment for GUI
ENV DISPLAY=:0
