FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN pip install fastapi gunicorn pydantic flake8 black pytest pre-commit
COPY ./app /app
