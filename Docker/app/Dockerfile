FROM python:latest as dev

RUN useradd -G www-data user

ENV HOME=/usr/src/www
ENV APP_HOME=/usr/src/www/app

WORKDIR "${APP_HOME}"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
 && apt-get install -y gettext

RUN pip install --upgrade pip
COPY ./Docker/app/source/requirements.txt .
RUN pip install -r requirements.txt
COPY ./Docker/app/source/requirements-devonly.txt .
RUN pip install -r requirements-devonly.txt


FROM dev as prod

RUN pip uninstall -y -r requirements-devonly.txt

COPY ./Docker/app/source .

RUN rm requirements.txt \
 && rm requirements-devonly.txt \
 && rm README.md \
 && rm -r teambuilding/www/tests

USER user