FROM python:3.9.13

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry install

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
