FROM python:3.11
WORKDIR /app
COPY app/src/requirements.txt .
RUN pip install --no cache dir -r requirements.txt
COPY app/src/ .
CMD ["python", "main.py"]
