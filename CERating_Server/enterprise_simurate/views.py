from __future__ import absolute_import
import time
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.shortcuts import render
from django.http import JsonResponse
from decimal import *
from enterprise_simurate.models import Enterprise, EnterpriseData, OfficialRatingGrade, Order

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


def getEnterprseRating(request):
    Ename = request.POST.get("name")

    dict = {"轻度污染":"A","中度污染":"B","重度污染":"C",}
    # 如果没有公司名字
    if OfficialRatingGrade.objects.filter(name=Ename).exists()==False:
        data = {"code": 1, "rate":"", "msg":"Unknown Enterprise Name"}
        return JsonResponse(data)
    oob = OfficialRatingGrade.objects.get(name=Ename)
    rate = dict.get(oob.classify)
    data={"code":0, "rate": rate}
    return JsonResponse(data)

def getEnterpriseRatingData(request):
    Email = request.POST.get("email")
    Ename = request.POST.get("name")
    session_key = request.session.session_key 
    # 如果没有登录
    if not request.session.exists(session_key): #session_key就是那个sessionid的值
        data = {"code":"1","data":" ","msg":"Not login"}
        return JsonResponse(data)
    # 另一种判断是否登录的方法
    # if request.session['is_login'] != True:
    #     data = {"code":"1", "msg":"未登录"}
    #     return JsonResponse(data)
    # 被查询的企业不存在
    if OfficialRatingGrade.objects.filter(name=Ename).exists()==False:
        data = {"code": "2","data":" ","msg":"Unknown Enterprise Name"}
        return JsonResponse(data)

    owner = Enterprise.objects.get(email=Email)
    goods = Enterprise.objects.get(name=Ename)
    # 当前用户并没有购买这个企业的信息
    if Order.objects.filter(owner_id=owner.id, goods_id=goods.id).exists()==False:
        data = {"code":"3","data":"","msg":"Didn't buy it"}
        return JsonResponse(data)
    
    goods_info = EnterpriseData.objects.get(id=goods.id)
    detail = {  "co2_emission":goods_info.co2_emission,
                "environmental_protection_input":goods_info.environmental_protection_input,
                "energy_onsumption":goods_info.energy_onsumption,
                "wastewater_discharge":goods_info.wastewater_discharge,
                "waste_discharge":goods_info.waste_discharge,
                "cod_discharge":goods_info.cod_discharge,
                "revenuein2020":goods_info.revenuein2020,
                "r_d_input":goods_info.r_d_input}
    data = {"code":0, "data":detail, "msg":""}
    return JsonResponse(data)

def purchaseRatingData(request):
    Email = request.POST.get("email")
    goods_name = request.POST.get("name")
    session_key = request.session.session_key 
    # 如果没有登录
    if not request.session.exists(session_key): #session_key就是那个sessionid的值
        data = {"code":"1"}
        return JsonResponse(data)
    owner = Enterprise.objects.get(email=Email)
    goods = Enterprise.objects.get(name=goods_name)
    # 余额不足
    if owner.balance < 10:
        data = {"code":"1"}
        return JsonResponse(data)
    
    owner.balance = owner.balance - 10
    owner.save()
    order = Order()
    order.owner_id = owner.id
    order.goods_id = goods.id
    order.save()

    data = {"code":"0"}
    return JsonResponse(data)

@require_POST
def test(request):
    session_key = request.session.session_key
    # 如果没有登录
    if not request.session.exists(session_key): #session_key就是那个sessionid的值
        data = {"code":"1"}
        request.session['is_login'] = True
        return JsonResponse(data)
    else:
        data = {"code":"2"}
        return JsonResponse(data)

    