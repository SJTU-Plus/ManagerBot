import logging
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

import aiosmtplib


class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, sender: str, passwd: str):
        self.sender = sender
        self.passwd = passwd
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    async def send_email(self, receiver: str, qq: str, code: str) -> bool:
        body = f'''
同学你好：
    你的加群验证码是：
    {code}
    它与你的QQ号{qq}绑定，请勿他用。你只需要申请一次验证码，便能通过所有群的验证，无需再次申请。验证码的有效期为30天，过期后需要重新申请。
    如果该申请不是由你发起的，请忽略此邮件。
                    SJTU学科群团队
'''
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = formataddr(('SJTU学科群团队', self.sender))
        message['To'] = formataddr((receiver, receiver))
        message['Subject'] = Header('SJTU学科群验证码', 'utf-8')
        try:
            async with aiosmtplib.SMTP(self.smtp_server, self.smtp_port, use_tls=True) as smtpobj:
                await smtpobj.login(self.sender, self.passwd)
                await smtpobj.sendmail(self.sender, receiver, message.as_string())
                logging.info(f'向{receiver}发送验证码成功！')
                return True
        except aiosmtplib.SMTPException as e:
            logging.warning(f'向{receiver}发送验证码失败：{e}')
            return False
