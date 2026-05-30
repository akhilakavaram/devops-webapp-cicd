FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

COPY app ./app
COPY tests ./tests

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import json, urllib.request; data=json.load(urllib.request.urlopen('http://127.0.0.1:8000/health')); raise SystemExit(0 if data['status'] == 'ok' else 1)"

CMD ["python", "-m", "app.main"]
