FROM python:alpine AS base
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/venv

RUN adduser -u 5678 --disabled-password --gecos "" appuser \
    && mkdir ${VIRTUAL_ENV} \
    && chown -R appuser ${VIRTUAL_ENV}

USER appuser

RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt

USER root
RUN chown -R appuser /app

USER appuser


#---------------------------------------------------------
FROM base AS prod

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "web.wsgi"]


#---------------------------------------------------------
FROM base AS dev

RUN pip install debugpy

CMD ["debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "manage.py", "runserver", "0.0.0.0:8000", "--nothreading", "--noreload"]