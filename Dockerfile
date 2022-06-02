FROM python:3.9.13

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
