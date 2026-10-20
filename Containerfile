FROM python:3.11-slim
WORKDIR /opt/app
COPY app/ ./app/
EXPOSE 8000
CMD ["python", "app/server.py"]
