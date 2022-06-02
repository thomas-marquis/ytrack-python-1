FROM python:3.10.4

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
