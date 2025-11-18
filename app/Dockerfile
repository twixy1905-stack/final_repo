FROM python:3.11

WORKDIR /app

# requirements.txt lives next to this Dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# your code is in src/, where main.py lives
COPY src/ .

# Run uvicorn HTTP server, binding to 0.0.0.0:80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
