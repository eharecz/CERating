from django.http import HttpResponse
import uuid
import time
from emailcheck.models import Emailcheck
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def hello(request):
    return HttpResponse("Hello World!")

@csrf_exempt
def email_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # 邮箱
        code = str(uuid.uuid1().int)[:6]  # 验证码
        timestamp = time.time() + 180  # 过期时间戳
        mail_host = "smtp.163.com"
        mail_user = "CERating@163.com"
        mail_pass = "SXMAUZBOKGBXDDVQ"
        sender = "CERating@163.com"
        receivers = [email]

        message = MIMEText(code, 'plain', 'utf-8')
        message['From'] = mail_user
        message['To'] = email
        subject = 'Verification Code'
        message['Subject'] = Header(subject, 'utf-8')
        smtpObj = smtplib.SMTP_SSL("smtp.163.com")
        smtpObj.connect(mail_host, 465)
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        check_record = Emailcheck.objects.filter(email=email)
        if check_record.exists():  # 如果表内有该邮箱的记录
            check_detail = Emailcheck.objects.get(email=email)
            check_detail.code = code
            check_detail.timestamp = timestamp
            check_detail.save()
        else:  # 如果没有该邮箱的记录
            new_record = Emailcheck(email=email, code=code, timestamp=timestamp)
            new_record.save()
        return HttpResponse()
