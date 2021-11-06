# Aisle Velocity
使用Docker容器技术一键启动OAR世界的Velocity反向代理  
（受到[cadwallion/mc-velocity-docker](https://github.com/cadwallion/mc-velocity-docker)的启发）  
## 构建说明
1. 使用openjdk:17-alpine作为基准,构建时下载最新velocity内核并创建环境；
2. 拷贝velocity.toml配置文件到镜像内；
## 前提条件
1. 腾讯云南京地域拥有容器计算资源和公网资源
2. 使用云联网接入OAR私有网络，详情请与weiruofeng@ruofengx.cn洽谈
3. 发布你接入点的IP

## 使用方法
在符合前提条件的机器上使用docker-compose运行本仓库中的docker-compose.yml配置即可  
