FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG USER_ID
ARG GROUP_ID

RUN groupadd -g "${GROUP_ID}" appuser \
 && useradd --no-log-init -m -r -u "${USER_ID}" -g appuser appuser

WORKDIR /app
USER appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

COPY ./source/requirements.txt /app/

RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir --user -r requirements.txt

COPY ./source /app