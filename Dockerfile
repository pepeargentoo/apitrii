FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
ADD requirements.txt /requirements.txt
COPY ./app /app
