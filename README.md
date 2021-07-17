 # ManagerBot

ManagerBot 是使用[NoneBot](https://github.com/nonebot/nonebot) 开发的QQ群管机器人。

它用来避免交大学科群混入非交大在校生的广告机器人。用户通过添加bot为好友申请与自己QQ绑定的验证码，该验证码将发送至用户的交大邮箱。用户加群时提交该验证码，Bot将验证用户输入的有效性，并自动决定放行与否。

 ## 如何使用
 ### 直接运行
 1. 下载并配置[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
 2. 创建 Python（>=3.7） 虚拟环境
     ```shell script
      virtualenv venv
      source venv/bin/activate
    ```
 3. 安装依赖
    ```shell script
    pip install -r requirements.txt
    ```
 4. 配置环境变量
    ```shell script
    export API_KEY=api_key
    export SUPER_USER=qq
    ```
 5. 运行`go-cqhttp`，运行`bot.py`
