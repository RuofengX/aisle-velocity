FROM ruby:3 AS builder
ARG VELOCITY_VERSION=3.1.1
COPY fetch-velocity.rb .
RUN ruby fetch-velocity.rb $VELOCITY_VERSION

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

COPY --from=builder velocity.jar .
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

COPY --from=builder velocity.jar .
# The Only difference with public service is using another config file 
COPY velocity-pp.toml ./velocity.toml
COPY run.sh .

ENTRYPOINT ["sh", "/opt/velocity/run.sh"]