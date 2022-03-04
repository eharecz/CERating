from django.shortcuts import render
from django.http import JsonResponse
from enterprise_recharge.models import Enterprise
from decimal import *

#输入email,rechargeAccount,若充值成功则返回{data:1}，充值失败返回{data:0}(金额为负数,或者不是整数)
# 若邮箱不存在，或者出现其他问题，则返回{data:2}
def recharge(request):
    em = request.POST.get('email')
    reA = request.POST.get('rechargeAccount') #获取rechargeAccount

    if Enterprise.objects.filter(email=em).exists()==False:#邮箱不存在
        data = {"code": 1}
        return JsonResponse(data)
    elif(reA is None):#如果充值金额没有输入
        data = {"code": 2}
        return JsonResponse(data)

    else:
        reA_dec = Decimal(reA)
        if(reA_dec.compare(Decimal(0))!=1 ):#如果充值金额小于等于0
            data = {"code": 3}
            return JsonResponse(data)
        else:
            oob = Enterprise.objects.get(email=em)
            oob.simulate_count = oob.simulate_count + reA_dec
            oob.save()
            data = {"code": 0}
            return JsonResponse(data)

# 充值接口
# 充值成功 :0
# 账户不存在 : 1
# 金额错误 ： 2
def recharge2(request):

    em = request.POST.get('email')

    if Enterprise.objects.filter(email=em).exists()==False:#邮箱不存在
        data = {"code": 1, 'msg': "邮箱不存在"}
        return JsonResponse(data)

    simulateCount = request.POST.get('simulateCount')
    money = request.POST.get('money')

    # 如果充值金额或次数为空
    if simulateCount is None or money is None:
        data = {"code": 2, 'msg': "充值金额/次数有误"}
        return JsonResponse(data)

    # 如果这里是小数会向下取整（希望前端可以让传过来的一定是整数
    simulateCountValue = Decimal(simulateCount)
    moneyValue = Decimal(money)

    # 如果充值金额或次数为负数
    if simulateCountValue < 0 or moneyValue < 0:
        data = {"code": 2, 'msg': "充值金额/次数有误"}
        return JsonResponse(data)
    else:
        oob = Enterprise.objects.get(email=em)
        oob.simulate_count = oob.simulate_count + simulateCountValue
        oob.balance = oob.balance + moneyValue
        oob.save()
        data = {"code": 0, 'msg': "充值成功"}
        return JsonResponse(data)
    
