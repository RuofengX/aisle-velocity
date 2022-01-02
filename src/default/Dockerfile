FROM openjdk:17-alpine

ENV TZ=Asia/Shanghai JAVA_MEMORY=256M
ARG VELOCITY_VERSION=3.0.1

RUN mkdir /opt/velocity
WORKDIR /opt/velocity

RUN set -ex \
    && wget -O velocity.jar https://versions.velocitypowered.com/download/${VELOCITY_VERSION}.jar \
    && mkdir plugins \
    && mkdir logs

COPY velocity.toml .
COPY run.sh .

EXPOSE 25565

ENTRYPOINT ["/opt/velocity/run.sh"]
