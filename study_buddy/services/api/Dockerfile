# Builder
FROM python:3.11-slim as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# Final Container
FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/api
RUN addgroup --system api_user && adduser --system --group api_user

ENV HOME=/home/api
ENV API_HOME=/home/api/app
ENV PYTHONPATH "${PYTHONPATH}:${API_HOME}"
RUN mkdir ${API_HOME}
WORKDIR ${API_HOME}

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY app/ $API_HOME

RUN chown -R api_user:api_user ${API_HOME}

USER api_user

CMD ["gunicorn", "main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
