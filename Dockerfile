FROM python:3.8.1

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y nano

# application folder
ENV APP_DIR /remarkably_code_test

# Copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ${APP_DIR}/requirements.txt

WORKDIR ${APP_DIR}

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . ${APP_DIR}

ENV FLASK_APP=remarkably/run.py

COPY start.sh ./
RUN chmod +x start.sh

CMD ["./start.sh"]

LABEL maintainer="nikola.komljenovic.work@gmail.com"