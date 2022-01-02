FROM openjdk:17-alpine

ENV TZ=Asia/Shanghai JAVA_MEMORY=256M
ARG VELOCITY_VERSION=3.1.1

RUN mkdir /opt/velocity
WORKDIR /opt/velocity

RUN set -ex \
    && wget -O velocity.jar https://papermc.io/api/v2/projects/velocity/versions/3.1.1/builds/98/downloads/velocity-3.1.1-98.jar \
    && mkdir plugins \
    && mkdir logs

COPY velocity.toml .
COPY run.sh .

EXPOSE 25565

ENTRYPOINT ["/opt/velocity/run.sh"]
