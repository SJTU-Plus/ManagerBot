# ManagerBot

ManagerBot 是使用[NoneBot](https://github.com/nonebot/nonebot) 开发的QQ群管机器人。

它用来避免交大学科群混入非交大在校生的广告机器人。用户通过添加bot为好友申请与自己QQ绑定的验证码，该验证码将发送至用户的交大邮箱。用户加群时提交该验证码，Bot将验证用户输入的有效性，并自动决定放行与否。

## 如何使用

需要同时运行go-cqhttp和Bot，方法分别如下。
### 配置[go-cqhttp](https://github.com/Mrs4s/go-cqhttp) （以 1.0.0-beta4 版在 Windows x64 系统上为例）
1. 下载 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
2. 运行`go-cqhttp_windows_amd64.exe`，按提示操作，将会生成`config.yml`。注意通信方式选择 **反向 WebSocket** 通信。
3. 修改`config.yml`，修改以下字段。如果在本机同时运行 Bot 和 go-cqhttp ，则把`ws://your_websocket_universal.server`改成`ws://127.0.0.1:8080/ws`。Bot 默认使用 8080 端口，可在Bot的`config.py`中修改`PORT`。
```yaml
account: # 账号相关
  uin: 1233456 # QQ账号
  password: '' # 密码为空时使用扫码登录
...
servers:
  # 添加方式，同一连接方式可添加多个，具体配置说明请查看文档
  # 反向WS设置
  - ws-reverse:
      # 反向WS Universal 地址
      # 注意 设置了此项地址后下面两项将会被忽略
      universal: ws://your_websocket_universal.server
```
4. 再次运行`go-cqhttp_windows_amd64.exe`，按提示操作，完成登录。

注意：当Bot使用的账号加入了新的群聊之后，需要重启go-cqhttp以刷新状态。
### 配置Bot
1. 创建 Python（>=3.7） 虚拟环境
    ```shell script
     virtualenv venv
     source venv/bin/activate
   ```
2. 安装依赖
   ```shell script
   pip install -r requirements.txt
   ```
3. 配置环境变量
   ```shell script
   export API_KEY=api_key
   export SUPER_USER=qq
   ```
4. 运行`bot.py`
