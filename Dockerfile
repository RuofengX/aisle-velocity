FROM ruby:3 AS builder
ARG VELOCITY_VERSION=3.1.1
COPY fetch-velocity.rb .
RUN ruby fetch-velocity.rb $VELOCITY_VERSION

FROM adoptopenjdk/openjdk11:alpine-slim
RUN mkdir /velocity
WORKDIR /velocity
RUN mkdir plugins
RUN mkdir logs

CMD ["/velocity/run.sh"]

#==============================================

FROM openjdk:17-alpine AS public
ENV TZ=Asia/Shanghai JAVA_MEMORY=256M
RUN apk add --no-cache tzdata

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
RUN apk add --no-cache tzdata

RUN mkdir /opt/velocity
WORKDIR /opt/velocity

RUN mkdir plugins
RUN mkdir logs

COPY --from=builder velocity.jar .
# The Only difference with public service is using another config file 
COPY velocity-pp.toml ./velocity.toml
COPY run.sh .

ENTRYPOINT ["sh", "/opt/velocity/run.sh"]