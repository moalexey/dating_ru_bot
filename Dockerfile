FROM python
RUN apt-get update \
    && apt-get -y install nano

RUN mkdir /project
RUN mkdir /project/dating_ru_bot

ADD . /project/dating_ru_bot

WORKDIR /project/dating_ru_bot
