FROM jetblackpope/pybuntu:3.8-focal

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install --no-install-recommends --no-install-suggests -y \
    apt-utils \
    dialog \
    ca-certificates

RUN  apt-get install --no-install-recommends --no-install-suggests -y \
        postgresql-client \
        libpq-dev \
        git \
        gpg \
        build-essential \
        iproute2 \
        libssl1.1 \
        lsb-release


RUN python -m pip install pip pipenv --upgrade

WORKDIR /code

COPY . .

COPY ./docker/production/fastapi/entrypoint /entrypoint

COPY ./docker/production/fastapi/start /start

RUN pipenv install --system
