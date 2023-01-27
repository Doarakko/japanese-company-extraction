FROM python:3.9

RUN apt -y update && \
  apt install -y mecab && \
  apt -y upgrade && \
  apt install -y libmecab-dev && \
  apt install -y mecab-ipadic-utf8 && \
  apt install -y git && \
  apt install -y make && \
  apt install -y curl && \
  apt install -y xz-utils && \
  apt install -y file && \
  apt install -y sudo

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
  cd mecab-ipadic-neologd && \
  ./bin/install-mecab-ipadic-neologd -n -y -p /usr/local/lib/mecab/dic/mecab-ipadic-neologd

WORKDIR /usr/local/lib/mecab/dic/user_dict
RUN wget https://s3-ap-northeast-1.amazonaws.com/chakki.jcl.jp/public/jcl_slim_mecab.dic.zip
RUN unzip jcl_slim_mecab.dic.zip

WORKDIR /app
COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml
RUN pip install -U pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
RUN rm -rf ~/.cache

COPY ./mecabrc /usr/local/etc/mecabrc
