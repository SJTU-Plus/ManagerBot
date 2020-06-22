 # ManagerBot

ManagerBot 是使用[NoneBot](https://github.com/nonebot/nonebot) 开发的QQ群管机器人。

它用来避免交大学科群混入非交大在校生的广告机器人。用户通过添加bot为好友申请与自己QQ绑定的验证码，该验证码将发送至用户的交大邮箱。用户加群时提交该验证码，Bot将验证用户输入的有效性，并自动决定放行与否。

 ## 如何使用
 
 1. 下载[酷Q](https://cqp.cc/b/news)
 2. 下载并安装[CoolQ HTTP API](https://github.com/richardchien/coolq-http-api) 插件。配置教程：(https://richardchien.gitee.io/coolq-http-api/docs/)
 3. 创建 Python（>=3.7） 虚拟环境
     ```shell script
      virtualenv venv
      source venv/bin/activate
    ```
 4. 安装依赖
    ```shell script
    pip install -r requirements.txt
    ```
 5. 登录酷Q程序，启用 CQ 插件，运行`bot.py`
