# CertExpireNotification

批量查询域名 SSL 证书到期时间，并通过 cqhttp 或邮件发送查询结果，提醒及时更换域名证书。

### 使用方法

1. 在 `main.py` 填写需要查询的域名，设置报警阈值
2. 在 `notification.py` 中填写你需要的发信方式，支持 cqhttp 和邮件。
3. 定时运行 `main.py` 即可。

### 所需模块

- requests
    - `pip install requests`
