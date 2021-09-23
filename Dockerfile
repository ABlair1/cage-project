FROM python:3.9-slim

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app

# install additional packages and dependencies
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
        libxslt-dev \
        musl-dev libffi-dev && \
        pip install --upgrade pip && \
        pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "nic_uncaged/manage.py", "runserver", "0.0.0.0:8000"]