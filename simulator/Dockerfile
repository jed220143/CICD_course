FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY simulator.py .

RUN addgroup --system app \
    && adduser --system --ingroup app app \
    && mkdir -p /app/out \
    && chown -R app:app /app/out

USER app

CMD ["python", "simulator.py"]
