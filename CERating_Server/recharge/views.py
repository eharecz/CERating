from django.shortcuts import render

from django.http import JsonResponse
from recharge.models import Enterprise
from decimal import *

#输入email,rechargeAccount,若充值成功则返回{data:1}，充值失败返回{data:0}(金额为负数,或者不是整数)
# 若邮箱不存在，或者出现其他问题，则返回{data:2}
def recharge(request):
    em = request.POST.get('email')
    reA = request.POST.get('rechargeAccount') #获取rechargeAccount


    if Enterprise.objects.filter(email=em).exists()==False:#邮箱不存在
        data = {"code":2}
        return JsonResponse(data)
    elif(reA is None):#如果充值金额没有输入
        data = {"code": 0}
        return JsonResponse(data)

    else:
        reA_dec = Decimal(reA)
        if(reA_dec.compare(Decimal(0))!=1 ):#如果充值金额小于等于0
            data = {"code":0}
            return JsonResponse(data)
        else:
            oob = Enterprise.objects.get(email=em)
            oob.balance = Decimal(oob.balance) + reA_dec
            oob.save()
            data = {"code": 1}
            return JsonResponse(data)
