import smtplib
import os
import zipfile
import tempfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
from configs.email_config import EMAIL_CONFIG

class EmailReporter:
    @staticmethod
    def send_report(allure_html_dir, report_name=None):
        """发送Allure HTML测试报告邮件"""
        try:
            # 验证HTML报告目录是否存在
            if not os.path.exists(allure_html_dir):
                raise FileNotFoundError(f"Allure HTML报告目录不存在: {allure_html_dir}")

            # 检查是否为有效的Allure HTML报告
            if not EmailReporter._is_valid_allure_html_report(allure_html_dir):
                raise ValueError(f"目录不是有效的Allure HTML报告: {allure_html_dir}")

            # 创建邮件对象
            msg = MIMEMultipart()
            msg['From'] = EMAIL_CONFIG['sender_email']
            msg['To'] = ', '.join(EMAIL_CONFIG['receiver_emails'])

            # 生成报告名称
            if not report_name:
                report_name = f"测试报告_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

            msg['Subject'] = f"{EMAIL_CONFIG['subject']} - {report_name}"

            # 添加邮件正文
            body_text = EMAIL_CONFIG['body_text'] + f"\n\n报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            body = MIMEText(body_text, 'plain', 'utf-8')
            msg.attach(body)

            # 准备并添加HTML报告附件（压缩为zip）
            zip_path = EmailReporter._prepare_html_report_zip(allure_html_dir, report_name)
            EmailReporter._add_attachment(msg, zip_path)

            # 发送邮件
            EmailReporter._send_email(msg)
            print(f"✓ Allure报告邮件发送成功！报告: {report_name}")

            # 清理临时zip文件
            if os.path.exists(zip_path):
                os.remove(zip_path)
                print(f"✓ 临时文件已清理: {os.path.basename(zip_path)}")

        except Exception as e:
            print(f"✗ 邮件发送失败: {str(e)}")
            raise

    @staticmethod
    def _is_valid_allure_html_report(report_dir):
        """检查是否为有效的Allure HTML报告目录"""
        # Allure HTML报告关键文件
        required_files = ['index.html']
        important_files = ['app.js', 'styles.css', 'data']

        # 必须要有index.html
        if not os.path.exists(os.path.join(report_dir, 'index.html')):
            print("✗ 缺少index.html文件")
            return False

        # 检查其他重要文件，但不强制要求（有些版本的Allure可能文件结构不同）
        missing_files = []
        for file in important_files:
            file_path = os.path.join(report_dir, file)
            if not os.path.exists(file_path):
                missing_files.append(file)

        if missing_files:
            print(f"⚠ 缺少一些文件（可能影响报告显示）: {', '.join(missing_files)}")

        return True

    @staticmethod
    def _prepare_html_report_zip(html_dir, report_name):
        """将HTML报告目录压缩为zip文件"""
        # 创建临时zip文件
        temp_dir = tempfile.gettempdir()
        zip_path = os.path.join(temp_dir, f"{report_name}.zip")

        print(f"📦 正在压缩报告目录: {html_dir}")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(html_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 在zip文件中保持相对路径
                    arcname = os.path.relpath(file_path, html_dir)
                    zipf.write(file_path, arcname)

        # 检查zip文件大小
        file_size = os.path.getsize(zip_path) / (1024 * 1024)  # MB
        print(f"📊 压缩完成，文件大小: {file_size:.2f} MB")

        return zip_path

    @staticmethod
    def _add_attachment(msg, file_path):
        """添加附件到邮件"""
        try:
            with open(file_path, 'rb') as file:
                filename = os.path.basename(file_path)
                part = MIMEApplication(file.read(), Name=filename)
                part['Content-Disposition'] = f'attachment; filename="{filename}"'
                msg.attach(part)
            print(f"📎 已添加附件: {filename}")
        except Exception as e:
            print(f"✗ 添加附件失败 {file_path}: {str(e)}")
            raise

    @staticmethod
    def _send_email(msg):
        """发送邮件"""
        try:
            print("🔗 正在连接SMTP服务器...")

            # 连接SMTP服务器
            if EMAIL_CONFIG['use_ssl']:
                server = smtplib.SMTP_SSL(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
            else:
                server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
                server.starttls()  # 启用TLS加密

            print("🔐 正在登录邮箱...")
            # 登录邮箱
            server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])

            print("📤 正在发送邮件...")
            # 发送邮件
            server.send_message(msg)

            # 关闭连接
            server.quit()
            print("✅ 邮件发送完成！")

        except smtplib.SMTPAuthenticationError:
            raise Exception("邮箱认证失败，请检查用户名和密码/授权码")
        except smtplib.SMTPConnectError:
            raise Exception("连接SMTP服务器失败，请检查网络和SMTP配置")
        except Exception as e:
            raise Exception(f"发送邮件时发生错误: {str(e)}")

    @staticmethod
    def check_email_config():
        """检查邮件配置是否完整"""
        required_fields = [
            'smtp_server', 'smtp_port', 'sender_email',
            'sender_password', 'receiver_emails'
        ]

        missing_fields = []
        for field in required_fields:
            if field not in EMAIL_CONFIG or not EMAIL_CONFIG[field]:
                missing_fields.append(field)

        if missing_fields:
            return False, f"缺少邮件配置: {', '.join(missing_fields)}"

        return True, "邮件配置完整"

    @staticmethod
    def test_connection():
        """测试邮件连接"""
        try:
            print("🧪 测试邮件配置...")
            is_valid, message = EmailReporter.check_email_config()
            if not is_valid:
                return False, message

            # 测试SMTP连接
            if EMAIL_CONFIG['use_ssl']:
                server = smtplib.SMTP_SSL(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
            else:
                server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
                server.starttls()

            server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
            server.quit()

            return True, "邮件配置测试通过"

        except Exception as e:
            return False, f"邮件配置测试失败: {str(e)}"


# 使用示例
if __name__ == "__main__":
    # 测试邮件配置
    success, message = EmailReporter.test_connection()
    print(message)

    if success:
        # 发送Allure HTML报告
        EmailReporter.send_report(allure_html_dir="../reports/allure_report",report_name="UI自动化测试报告")