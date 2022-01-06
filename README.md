# Aisle Velocity
Run velocity using docker-compose by one click.  
(Inspired by [cadwallion/mc-velocity-docker](https://github.com/cadwallion/mc-velocity-docker))  
使用Docker容器技术一键启动OAR世界的Velocity反向代理，受到[cadwallion/mc-velocity-docker](https://github.com/cadwallion/mc-velocity-docker)的启发  
## Dockerfile说明
使用多阶段构建，  
第一阶段builder: 使用Python3环境运行fetch-paper-api获取最新JAR文件  
第二阶段public: 将第一阶段JAR文件拷贝到openjdk:17-alpine中，拷贝velocity-public.toml配置文件到镜像内；  
第三阶段proxy-protocol: 将第一阶段JAR文件拷贝到openjdk:17-alpine中，拷贝velocity-pp.toml配置文件到镜像内。  

## docker-compose.yml说明
将第二、第三阶段镜像分别创建两个服务，分别运行在25565和60000端口。前者直接接受客户端连接，后者接受包含proxy-protocol的来自其他四层代理的封包。

## fetch-paper-api.py说明
来自
## 使用方法
在内网机器上运行`docker-compose up -d --build`。如不需要proxy-protocol服务，请自行修改docker-compose配置文件，删除对应服务即可。  
