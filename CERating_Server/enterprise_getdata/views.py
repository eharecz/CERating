import json
from django.http import HttpResponse
from django.http import JsonResponse
from enterprise_getdata.models import OfficialRatingGrade
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getEnterpriseData(request):
    if request.method == 'POST':
        result = {"enterprise": [], "year": 2020}
        data = OfficialRatingGrade.objects.all()
        print(data.values())
        # 序列化为 Python 对象
        obj = serializers.serialize('python', data)
        for item in obj:
            result["enterprise"].append(item["fields"]["name"])
        # 转换为 JSON 字符串并返回
        # return HttpResponse(result, content_type="application/json")
        # return HttpResponse(json.dumps(result), content_type="application/json")
        return JsonResponse(result)
