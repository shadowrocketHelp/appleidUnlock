
[![AppleID_Unlock.png](https://github.com/shadowrocketHelp/appleidUnlock/blob/main/img/apidun2.png?raw=true)]()

# AppleID Unlock 更新时间 2023年2月26日
全新自动解锁苹果Apple ID账号 自动解锁 自动关闭手机双重验证 自动删除设备 自动适配密保安全问题 定时任务

### 功能：
* 自动解锁 Apple ID 账号【已开发完毕】
* 自动关闭 Apple ID 双重验证【已开发完毕】
* 自动修改 Apple ID 账号密码【已开发完毕】
* html一键分享  【已开发完毕】
* 自动删除 Apple ID 多余设备【已开发完毕】
* telegram 通知【已开发完毕】优化通知推送状态，正常/不正常 可选
* 相关 api 接口  (开发中)
* 自定义html内容 （开发中）

### 使用教程 （下面二选一即可）
#### 【一】纯新手小白版本
* (注册码需加 [Telegarm 群](https://t.me/apidlock) 免费获取）

#### 【二】自己服务器部署
* 准备一台 Debian 11 服务器/VPS
* 设置时区 并 安装aapanle
```
apt -y install ntpdate
timedatectl set-timezone Asia/Shanghai
ntpdate ntp1.aliyun.com
apt install -y wget && wget -O install.sh http://www.aapanel.com/script/install_6.0_en.sh && bash install.sh

```
* 登录aapanle 并极速安装以下软件
```
nginx 1.20.1
php 7.4
MySQL 5.6
phpMyAdmin 4.9
```
* php设置 删除禁用函数```shell_exec```
* 准备一个域名解析到服务器id地址，```aapanle-网站-添加站点-数据库创建MySQL```
* 下载代码
```
教程完善中...
```
* 上传数据库（教程完善中...
* 配置文件（教程完善中...

### 常见问题
* 【问1】为什么不能删除绑定手机/二次验证
* 【答1】必须要有 ```donnot recognize this number?```（不认识这个号码吗？）提示才可以删除。参考下面两个图片，自行对比。目前我们会提示```此账号无法通过密保删除手机二次验证，请更换账号```

 [![AppleID_Unlock.png](https://github.com/shadowrocketHelp/appleidUnlock/blob/main/img/phone1.png?raw=true)]()
 
 [![AppleID_Unlock.png](https://github.com/shadowrocketHelp/appleidUnlock/blob/main/img/phone2.png?raw=true)]()

