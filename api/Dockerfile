FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production
ENV APP_PORT=8000
ENV LOG_LEVEL=INFO

WORKDIR /app

COPY pyproject.toml README.md ./
COPY app ./app

RUN pip install --no-cache-dir .

RUN addgroup --system app && adduser --system --ingroup app app
USER app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
