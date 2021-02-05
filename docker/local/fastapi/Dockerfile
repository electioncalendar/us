FROM jetblackpope/pybuntu:3.8-focal

ARG DEBIAN_FRONTEND=noninteractive

ARG USERNAME=code
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install a couple python "system" packages
RUN python -m pip install pip pipenv black isort apt-select --upgrade

# Find a faster mirror cause the achrive ones are almost always super slow
RUN apt-select \
    && cp /etc/apt/sources.list /etc/apt/sources.list.backup \
    && mv sources.list /etc/apt/

RUN apt-get update

RUN apt-get install --no-install-recommends --no-install-suggests -y \
    apt-utils \
    dialog \
    ca-certificates

RUN apt-get install --no-install-recommends --no-install-suggests -y \
    git \
    gpg \
    openssh-client \
    less \
    iproute2 \
    procps \
    curl \
    wget \
    lsb-release \
    build-essential \
    libssl1.1 \
    libpq-dev \
    postgresql-client \
    htop

# Should probably write this into some sort of bash script that reads in vars
# and doesn't always do all the things.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && apt-get install --no-install-recommends --no-install-suggests -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN echo "export PROMPT_COMMAND='history -a'" >> "/root/.bashrc" \
    && echo "export HISTFILE=/commandhistory/.bash_history_root" >> "/root/.bashrc" 

RUN echo "export PROMPT_COMMAND='history -a'" >> "/home/code/.bashrc" \
    && echo "export HISTFILE=/commandhistory/.bash_history_code" >> "/home/code/.bashrc"

ENV PYTHONPATH="/code/api"

WORKDIR /code