FROM python:3 AS builder
WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ARG PROJECT='velocity'
ARG VERSION='3.1.1'

COPY ./scripts/fetch-paper-api/fetch-paper-api.py .
RUN python fetch-paper-api.py $PROJECT $VERSION

#==============================================

FROM openjdk:17-alpine AS public
ENV TZ=Asia/Shanghai JAVA_MEMORY=256M
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk update &&\
    apk add --no-cache tzdata

RUN mkdir /opt/velocity
WORKDIR /opt/velocity

RUN mkdir plugins
RUN mkdir logs

COPY --from=builder target.jar ./velocity.jar
COPY velocity-public.toml ./velocity.toml
COPY run.sh .

ENTRYPOINT ["sh", "/opt/velocity/run.sh"]

#==============================================

FROM openjdk:17-alpine AS proxy-protocol
ENV TZ=Asia/Shanghai JAVA_MEMORY=256M
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk update &&\
    apk add --no-cache tzdata
RUN mkdir /opt/velocity
WORKDIR /opt/velocity

RUN mkdir plugins
RUN mkdir logs

COPY --from=builder target.jar ./velocity.jar
# The Only difference with public stage is using another config file 
COPY velocity-pp.toml ./velocity.toml
COPY run.sh .

ENTRYPOINT ["sh", "/opt/velocity/run.sh"]