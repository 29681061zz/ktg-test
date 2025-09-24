# 邮件配置信息
EMAIL_CONFIG = {
    # SMTP服务器配置
    #'smtp_server': 'smtp.163.com',  # SMTP服务器地址
    'smtp_server': 'smtp.qq.com',  # QQ邮箱
    'smtp_port': 465,  # SMTP端口，SSL一般为465，TLS为587
    'use_ssl': True,  # 是否使用SSL加密

    # 发件人配置
    'sender_email': 'xxxx@qq.com',  # 发件人邮箱
    'sender_password': 'xxxxxx',  # 邮箱密码或授权码

    # 收件人配置
    'receiver_emails': [  # 收件人邮箱列表
        'xxxxxx@qq.com',
    ],

    # 邮件内容配置
    'subject': '自动化测试报告 - Allure',  # 邮件主题
    'body_text': '''您好，

本次自动化测试已完成，附件是Allure HTML测试报告。

报告包含：
- 测试用例执行情况（通过率、失败率）
- 详细的失败原因和截图
- 测试执行时长统计
- 环境信息和日志

请下载附件后解压，用浏览器打开 index.html 查看完整报告。

此邮件由自动化测试系统自动发送。
''',  # 邮件正文
}