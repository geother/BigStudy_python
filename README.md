> 自用，脚本更改自[yuzaii/JsQndxx_Python: 江苏省青年大学习自动学习Python脚本](https://github.com/yuzaii/JsQndxx_Python)，增加workflow与secret key配置。

fork本仓库，然后在`Settings`→`Security`→`Secrets`→`Actions`选项卡中，添加`New repository secret`：

- `COOKIE`为`COOKIE`
- `SEND_KEY`为`Server酱SEND_KEY`

🎈[Sever酱](https://sct.ftqq.com/sendkey)

默认每天UTC时间13时运行，每周一向微信推送结果。（[yuzaii](https://github.com/yuzaii)指出每天都执行脚本，则laravel_session不会改变）
