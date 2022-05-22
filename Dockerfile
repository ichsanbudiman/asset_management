FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
RUN apt-get update
RUN apt-get install curl netcat -y
RUN pip install fastapi uvicorn requests python-multipart minio
# nc -vz db 3306
WORKDIR /src

COPY ./src /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
