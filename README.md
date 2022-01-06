# Aisle Velocity
Run velocity using docker-compose by one click.
## 中文说明
使用Docker容器技术一键启动OAR世界的Velocity反向代理  
（受到[cadwallion/mc-velocity-docker](https://github.com/cadwallion/mc-velocity-docker)的启发）  
## 构建说明
1. 使用Python3环境运行fetch-paper-api获取最新JAR文件
2. 将第一阶段JAR文件拷贝到openjdk:17-alpine中；
3. 拷贝velocity.toml配置文件到镜像内；
## 使用方法
在内网机器上运行docker-compose up -d --build即可  
