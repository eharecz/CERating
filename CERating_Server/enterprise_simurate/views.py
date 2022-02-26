from django.shortcuts import render
from django.http import JsonResponse
from enterprise_simurate.models import Enterprise
from decimal import *

#输入邮箱判断是不是有余额。如果有余额，则将数据库中的余额-price，并返回{data:1};余额不够则返回{data:0}。
# 若邮箱不存在，或者出现其他问题，则返回{data:1}
def enterprise_simurate(request):
    em = request.POST.get('email')  # 相关负责人邮箱地址

    # 若邮箱不存在，或者出现其他问题，返回{data:1}
    if Enterprise.objects.filter(email=em).exists()==False:
        data = {"code": 1}
        return JsonResponse(data)

    oob = Enterprise.objects.get(email=em)

    #余额不够则返回2
    if (oob.simulate_count <= 0 or oob.simulate_count is None):
        data = {"code": 2}
        return JsonResponse(data)

    #余额充足,查询成功，返回0
    else:
        oob.simulate_count = oob.simulate_count - 1            #查询次数+1
        oob.save()
        data = {"code": 0}
        return JsonResponse(data)

