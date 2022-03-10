import json
from django.http import HttpResponse
from enterprise_getdata.models import OfficialRatingGrade
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getEnterpriseData(request):
    if request.method == 'POST':
        result = []
        data = OfficialRatingGrade.objects.all()
        # 序列化为 Python 对象
        obj = serializers.serialize('python', data)
        for item in obj:
            item['fields']['year'] = 2020
            result.append(item['fields'])
        # 转换为 JSON 字符串并返回
        # return HttpResponse(result, content_type="application/json")
        return HttpResponse(json.dumps(result), content_type="application/json")
