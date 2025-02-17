# FROM python:3

# WORKDIR /home

# COPY . /home/

# RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "python", "./main.py" ]

FROM ubuntu:noble-20250127

WORKDIR /home

COPY ./* .

ENV LANG=c.UTF-8
ENV PATH=/root/.local/bin:$PATH

RUN apt update \
&& apt install -y python3 python3-pip pipx\  
&& pipx install pipenv \
&& pipenv --python /usr/bin/python3 \
&& pipenv install --deploy

ENTRYPOINT [ "pipenv", "run" ]
CMD [ "python3", "main.py" ]