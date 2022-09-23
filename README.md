> 自用，脚本更改自[yuzaii/JsQndxx_Python: 江苏省青年大学习自动学习Python脚本](https://github.com/yuzaii/JsQndxx_Python)，增加workflow与secret key配置。

fork本仓库，然后在`Settings`→`Security`→`Secrets`→`Actions`选项卡中，添加`New repository secret`：

- `Name`为`COOKIE`
- `Secret`为`抓包获得的cookie(不含引号)`

默认每日UTC时间13时运行。
