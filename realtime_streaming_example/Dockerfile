# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py ./

# Expose the streaming port
EXPOSE 5005

# Default environment variable
ENV PORT=5005

# Hugging Face token for gated repo access (replace with your token or override at runtime)
ENV HUGGINGFACE_HUB_TOKEN=your_token_here

# Run the Flask app
CMD ["python", "main.py"]
