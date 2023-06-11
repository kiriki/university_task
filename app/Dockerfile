FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-interaction --no-ansi --no-root --no-dev

COPY . /app

CMD ["uvicorn", "app.main_basic:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
