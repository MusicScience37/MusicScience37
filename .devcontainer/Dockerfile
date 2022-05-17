FROM musicscience37/pipenv:focal-v2.4

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-client \
    gnupg2 \
    vim \
    nano && \
    apt-get autoremove && \
    apt-get autoclean
