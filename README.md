# Aisle Velocity
Run velocity using docker-compose
## NOTICE
Do not leak ANY KEY in config file. I am running mygame in a local network, so it could work.  
## 中文说明
使用Docker容器技术一键启动OAR世界的Velocity反向代理  
（受到[cadwallion/mc-velocity-docker](https://github.com/cadwallion/mc-velocity-docker)的启发）  
## 构建说明
1. 使用openjdk:17-alpine作为基准,构建时下载最新velocity内核并创建环境；
2. 拷贝velocity.toml配置文件到镜像内；
## 使用方法
在符合前提条件的机器上使用docker-compose运行本仓库中的docker-compose.yml配置即可  
