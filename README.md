# 江苏省青年大学习自动学习Python脚本
> 每周都要被团支书催着做青年大学习，虽然网上也有很多办法可以秒过，但是还是得打开微信公众号然后点击最新一期的青年大学习。我就想能不能有办法每周自动帮我完成呢？本着能copy就不自己动手的原则，我在github逛了半天，结果并没有发现江苏省青年大学习自动学习相关代码，无奈只好自己写一个了。

## 使用教程

- 修改main.py中的laravel_session

```python
if __name__ == '__main__':
# 下方xxx填入你自己的laravel_session 长度为40的字母数字组合
    laravel_session = "xxx"
    qndxx = Qndxx(laravel_session)
    qndxx.login()
    qndxx.confirm()

```

- 运行main.py 

```bash
python main.py
```

## 自动部署

- 可以使用Github Actions部署
- 可以部署自己的服务器上（推荐）
- 如果你没有自己的服务器，也可以使用我给我们学校开发的网站（只要是江苏省的学校都可以用）https://ntutools.cn/ 注册即用 

<img src="https://file-1305871479.cos.ap-nanjing.myqcloud.com/img/202209172335530.png" alt="image-20220917233505745" style="zoom:50%;" />

##### 因为laravel_session每几天就会改变，但是如果你每天都执行一次，laravel_session就一直不会变，所以建议部署的时候最好是一天执行一次。（本人通过这个方法已经一个学期没有去管过青年大学习了）

## 实现原理

对于这种功能一般都和网络请求相关了，简单来说就是带着你的信息去发送请求即可。

## 开发过程

### 准备工作

+ ##### 抓包

  手机抓包教程见[我的博客](https://yuzai.xyz/archives/c59a0c1a.html)

  既然要发送请求，那肯定要知道向哪发送请求

  <img src="https://file-1305871479.cos.ap-nanjing.myqcloud.com/img/202204301653990.png" alt="image-20220317212319083" style="zoom:50%;" />

  <img src="https://file-1305871479.cos.ap-nanjing.myqcloud.com/img/202204301653543.png" alt="image-20220317210836350" style="zoom:50%;" />

  <img src="https://file-1305871479.cos.ap-nanjing.myqcloud.com/img/202204302000461.png" alt="image-20220317211344168" style="zoom:50%;" />

+ ##### 分析

  我通过Charles抓包发现每次的请求江苏省青年大学习的接口是https://service.jiangsugqt.org/youth/lesson

  确认课程的接口是https://service.jiangsugqt.org/youth/lesson/confirm

  外加一些参数，和一个带有laravel_session的cookie。我们只需要带着这些信息去请求就好了。

  一开始我没有加上laravel_session，发现并不能成功发送，卡在了微信客户端验证的页面，无论我如何修改ua，都不行，我才想到青年大学习就是通过cookie中的laravel_session来获取用户信息的，不带他发送请求肯定不行，果然带上他就可以获取到我的信息了。我们都知道cookie是储存在用户本地的数据，但是我到现在还是不知道他的生命周期是久，目前差不多一个星期了，还是没有过期，希望能久一点吧。laravel_session可不可以自己生成呢？以我现在的技术很难，第一是应为肯定加密过，第二因为客户端是微信，破解也很难(如果我能破解了我就准备去腾讯上班了)，所以还是老老实实抓包吧。

+ ##### 写代码（代码写的很糟糕希望后来者可以再度完善）

​		通过抓包，可以发现一共请求了两个接口，所以我们只要发送两个请求，一个是请求课程接口，方法是get，一个是确认用户信息的接口，方法是post。之后开开心心写代码就好了。

​		当我写到第二个请求的时候发现请求失败，仔细观察了一下，原来在第一个请求发送成功后，在响应体的js里面有一个token和lesson_id

<img src="https://file-1305871479.cos.ap-nanjing.myqcloud.com/img/202204302000219.png" alt="image-20220317213507633" style="zoom:50%;" />

我们只要获取他们，然后添加到参数中就可以了。成功的返回结果如下：

```json
{'message': '操作成功', 'status': 1, 'redirect': '', 'data': {'url': 'https://h5.cyol.com/special/daxuexi/cep3js1vq4/m.html'}}
```

### 另外，我还做了一个java版本的供大家参考https://github.com/yuzaii/Qndxx_Java

## 创作不易 希望能得到您一颗小星星⭐️ 万分感谢！

