FROM python:latest

WORKDIR /workspace

RUN pip install pex

WORKDIR /code

COPY bin .

RUN pip wheel -w . .

RUN pex --python=python3 -f $PWD $(cat requirements.txt) sample -e main -o example.pex

ENV WAIT_VERSION 2.7.2

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD ["./example.pex"]