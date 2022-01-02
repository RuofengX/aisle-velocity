# Aisle Velocity
Run velocity using docker-compose by one click.
## Services
When set up docker-compose, 2 service2 will start. One is for normal proxy on internet, running on port 25565; and another is for connect with proxy-protocol running on port 60000. You can add a nginx 4layer proxy before the second service. Also you can edit the docker-compose file to satisfy your own needs.  
The docker-compose-alt.yml file will start proxy-protocol only, for machine with low memory.  
Java memory limit is set in Dockerfile, you can change it to any value you want. the default is 256M, which is good for 10-100 players.  
Velocity config is src/default, and will be copied into image when build.

## 中文说明
使用Docker容器技术一键启动OAR世界的Velocity反向代理  
（受到[cadwallion/mc-velocity-docker](https://github.com/cadwallion/mc-velocity-docker)的启发）  
## 构建说明
1. 使用openjdk:17-alpine作为基准,构建时下载最新velocity内核并创建环境；
2. 拷贝velocity.toml配置文件到镜像内；
## 使用方法
在内网机器上运行docker-compose up -d --build即可  
