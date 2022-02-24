from django.shortcuts import render
from django.http import JsonResponse
from SimuRate_times_query.models import Enterprise
from decimal import *

#输入邮箱判断是不是有余额。如果有余额，则将数据库中的余额-price，并返回{data:1};余额不够则返回{data:0}。
# 若邮箱不存在，或者出现其他问题，则返回{data:2}
def SimuRate_times_query(request):
    em = request.POST.get('email')  # 相关负责人邮箱地址

    # 若邮箱不存在，或者出现其他问题，返回{data:2}
    if Enterprise.objects.filter(email=em).exists()==False:
        data = {"code":2}
        return JsonResponse(data)

    #余额不够则返回0,
    oob = Enterprise.objects.get(email=em)

    if (oob.balance <= 0 or oob.balance is None):
        data = {"code":0}
        return JsonResponse(data)

    #余额充足,查询成功，返回1
    else:
        oob.balance = Decimal(oob.balance)-Decimal(oob.price) #余额-价格
        oob.simulate_count = oob.simulate_count+1            #查询次数+1
        oob.save()
        data = {"code": 1}
        return JsonResponse(data)

