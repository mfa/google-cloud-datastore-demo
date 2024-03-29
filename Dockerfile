FROM tiangolo/uvicorn-gunicorn:python3.9-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY ./app /app
