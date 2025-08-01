FROM python:3.13.5-slim
ENV NODE_MAJOR=20
RUN useradd -ms /bin/sh -u 1001 code

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    ca-certificates \
    gnupg \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
    && apt-get update && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



RUN apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt package.json tailwind.config.js /code/
    
RUN pip install --upgrade pip \
    && pip install gunicorn \ 
    && pip install --no-cache-dir -r /code/requirements.txt

WORKDIR /code/
RUN npm install --omit=dev
RUN npm install concurrently --save-dev
RUN npm install -D @tailwindcss/line-clamp

USER code
COPY --chown=code:code requirements.txt package.json tailwind.config.js  /code/

RUN pip install --upgrade pip \
    && pip install gunicorn django-browser-reload \
    && pip install --no-cache-dir -r /code/requirements.txt