FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run gunicorn — log-file/access-logfile/capture-output all route to stdout
CMD ["gunicorn", "mydjango.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "2", \
     "--log-file", "-", \
     "--access-logfile", "-", \
     "--capture-output", \
     "--log-level", "debug"]
