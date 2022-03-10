import json
from django.shortcuts import render
from web.models import Enterprise
from django.http import JsonResponse

def login(request):
    try:
        user = Enterprise.objects.get(email=request.POST['email'])
        s = request.POST['password']
        if user.password == s:
            print('登录成功')
            data = {'code': 0, 'name': user.name}
            return JsonResponse(data)
        else:
            print("密码错误")
            data = {'code': 2, 'name': ''}
            return JsonResponse(data)
            
    except Exception as err:
        print('邮箱不存在')
        data = {'code': 1, 'name': ''}
        return JsonResponse(data)

