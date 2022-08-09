FROM python:3.8.5-alpine
RUN  pip install --upgrade pip

COPY requirements.txt .

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow 
    #&& apk del build-deps

RUN pip install -r requirements.txt
COPY ./ /project
WORKDIR /project

COPY entrypoint.sh /

ENTRYPOINT ["sh","/entrypoint.sh"]

