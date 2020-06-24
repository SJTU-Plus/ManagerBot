 # ManagerBot

ManagerBot 是使用[NoneBot](https://github.com/nonebot/nonebot) 开发的QQ群管机器人。

它用来避免交大学科群混入非交大在校生的广告机器人。用户通过添加bot为好友申请与自己QQ绑定的验证码，该验证码将发送至用户的交大邮箱。用户加群时提交该验证码，Bot将验证用户输入的有效性，并自动决定放行与否。

 ## 如何使用
 ### 直接运行
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
 5. 安装redis，保持端口为6379。
    ```shell script
    sudo apt install redis-server
    ```
    Windows 10上可以使用WSL运行redis。
 6. 登录酷Q程序，启用 CQ 插件
 7. 配置环境变量
    ```shell script
    export SMTP_SERVER=smtp.example.com
    export SMTP_PORT=465
    export SMTP_USER=me@example.com
    export SMTP_PASSWD=passwd
    export ATTESTATION_SECRET=secret
    export REDIS_HOST=localhost
    export SUPER_USER=qq
    ```
 7. 运行`bot.py`
 
 ### 使用docker compose
 请参考 [ManageBotDocker](https://github.com/SJTU-Plus/ManageBotDocker)
