# 主要流程


**adb截图-->orc识别题目-->百度答案**

# 环境准备
- [adb工具包](http://www.skycn.com/soft/appid/24272.html)
- [python3](https://www.python.org/downloads/)

## 安装adb工具包
将工具包装好后，将其路径加入环境变量

## 安装python
下载python3安装，打开命令行键入**pip install requests**,安装requests库

由于python的离线ocr库较慢，因此在阿里云上找了一个[orc接口](https://market.aliyun.com/products/57124001/cmapi023869.html?spm=5176.2020520132.101.4.OqWAJI#sku=yuncode1786900000)（很便宜，1分钱几百次）
，再把代码里的appcode换成自己的就行了

这样环境的撘好了
-------------

# 运行程序
- 手机连接电脑，打开usb调试
- 在cmd中运行下载的脚本运行，python getMyAnswer

# 没有意外的话我们的人工智障答题小助手就跑起来了
