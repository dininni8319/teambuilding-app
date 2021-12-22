FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG USER_ID
ARG GROUP_ID

RUN groupadd -g "${GROUP_ID}" user \
 && useradd --no-log-init -m -r -u "${USER_ID}" -g user user

ENV HOME=/home/user/www
ENV APP_HOME=/home/user/www/app

RUN mkdir -p "${APP_HOME}"
RUN mkdir "${APP_HOME}/static"

WORKDIR "${APP_HOME}"
RUN chown -R user:user "${HOME}"
USER user

ENV PATH="${HOME}/.local/bin:${PATH}"

# Nota: l'upgrade di pip va eseguito dopo aver impostato correttamente la variabile di ambiente PATH
RUN python -m pip install --upgrade pip

COPY ./source/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install django-debug-toolbar gunicorn

COPY ./source .
