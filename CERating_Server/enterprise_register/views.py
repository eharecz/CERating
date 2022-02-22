
import email
from django.http import JsonResponse
from django.shortcuts import render
from enterprise_register.models import Emailcheck, Enterprise
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.
@csrf_exempt
def Enterprise_Register(request):
    na = request.POST.get('name') #企业名称
    ty = request.POST.get('type') #企业类型
    re = request.POST.get('relation') #企业从属关系：0总公司、1分公司、2其他
    em = request.POST.get('email') #相关负责人邮箱地址
    pa = request.POST.get('password') #密码的sha256加密密文
    ca = request.POST.get('captcha') #注册邮箱验证码
    # print(Enterprise.objects.filter(email=em).exists())

    #判断邮箱是否存在，如果存在，则返回code，为1
    if Enterprise.objects.filter(email=em).exists()==True:
        data = {"code":1}
        return JsonResponse(data)

    #若不存在，则进行注册，判断验证码是否相同
    else:
        oob = Emailcheck.objects.get(email=em)
        if(str(oob.code) != ca):
            data = {"code":2}
            return JsonResponse(data)
        else: 
            ob = Enterprise()
            ob.id =  time.time() 
            ob.name = na
            ob.type = ty
            ob.relation = re
            ob.email = em
            ob.password = pa
            ob.simulate_count=0
            ob.save()
            data = {"code":0}
            return JsonResponse(data)