FROM python:3.13.5-slim-bullseye
RUN useradd -ms /bin/sh -u 1001 code

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /code/
    
RUN pip install --upgrade pip \
    && pip install gunicorn \ 
    && pip install --no-cache-dir -r /code/requirements.txt

USER code
WORKDIR /code/src
COPY --chown=code:code requirements.txt /code/

RUN pip install --upgrade pip \
    && pip install gunicorn django-browser-reload \
    && pip install --no-cache-dir -r /code/requirements.txt