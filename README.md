## 介绍

该程序的主要核心文件为huff_code文件夹下的huffman.py各种要求功能均已实现,除了界面的设计,该项目通过应用在网页在线加密聊天来代替窗口的设计(实际上是用HTML来在网页上设计窗口)

chat_online文件夹为对huffman.py的应用,主要技术为使用python的tornado的websocket来实现在线实时聊天.

## 环境说明

该项目使用python3实现Python3下载地址:https://www.python.org/downloads/

使用到的第三方库有 tornado,pymysql

第三方库的安装方式:

windows:打开cmd输入pip install tornado  (前提是Python安装时已经加入系统环境变量,pymysql安装同理)

Linux(一般Linux自带两个版本的Python):打开终端输入pip3 install tornado (pymysql同理)



## 运行说明

huff_code文件夹下的huffman.py可单独运行(内有大量注释)

chat_online文件夹下的在线聊天工程只需运行server.py文件

>### 注意
>
>需要修改chat_online/templates/home.html文件中`var ws = new WebSocket("ws://10.31.66.157:8000/chatroom");`
>
>将其中的IP改为你当前的IP,并使用两台或以上在同ip下的电脑或手机在浏览器访问网址,格式为 "你的ip:8000"
>
>另外,我没有给解密网页跳转链接,需要另开一个 "你的ip:8000/decode" 网页
>
>因为该项目有注册页面,需要使用数据库,这里使用的数据库为Mysql5.6;另外注意Mysql8.0以上好像和pymysql不兼容会报错.
>
>在数据库中创建名为users的表.内容为username和password这里给出创建命令
>
>`CREATE TABLE users(username varchar(1000), password varchar(1000));`
>
>注册时请勿使用中文
>
>并相应的在config.py下的数据库里改为你的设置
>
>```python
>mysql = {
>    "host": "",
>    "user": "",
>    "passwd": "",
>    "dbName": ""        # users表所属的库名
>}
>```



## 在聊天时的注意

**因为只对26个大写的英文字母和空格进行编码所以在输入其他的字符时会出错.**



## 另外

*网页部分只对注册页面进行css美化,所以视觉上可能不是特别美观*

如果运行时报huff_code为找到的错误请手动将huff_code文件夹下的huffman.py复制到chat_online文件夹下,并改动chat_onlie/views/index.py文件第7行 `from huff_code import huffman` 改为 `import huffman`保存之后再次运行server.py即可

