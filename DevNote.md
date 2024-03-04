
# Trader Workstation (TWS) API

https://www.interactivebrokers.com/en/trading/ib-api.php


https://github.com/atreyuxtrading/atreyu-backtrader-api


1、backtrader内置的盈透证券（Interactive Brokers）实盘交易api支持的是盈透证券老版本的api。github上有人开发了新的backtrader接口，支持盈透新的实盘api，称为atreyu-backtrader-api。 例子和用法说明见这里。

2、盈透证券的TWS工作站软件，是个可直接手工交易，也可设置端口供第三方软件连接TWSAPI程序化交易。

但TWS工作站软件比较庞大，占用资源比较多，程序化交易，我们直接下载简洁的IBGateWay网关程序，连接TWSAPI（手工下单使用盈透提供的手机APP)。