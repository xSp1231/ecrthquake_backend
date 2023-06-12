import json

from django.http import JsonResponse
from django.shortcuts import render
from datamanage.models import Province_eqnum, Province_intro


def getprovincedata(request):
    print(request.GET)
    name = request.GET.get('province')
    print("省份为 ", name)
    data = Province_eqnum.objects.filter(province=name).first()
    ydata = [data.num2013, data.num2014, data.num2015, data.num2016, data.num2017, data.num2018, data.num2019,
             data.num2020, data.num2021, data.num2022]
    print("ydata is ", ydata)
    return JsonResponse({"ydata": ydata})


def getprovinceintro(request):
    area=request.GET.get('area')
    data=Province_intro.objects.get(province=area)
    piedata=json.loads(data.pie_json)
    for it in  piedata:  # 更改键的名字
        it["name"]=it.pop("area")
    print("finanl ",piedata)
    dic={"injure":data.injurenum,"death":data.deathnum,"total":data.total,"intro":data.intro,"piedata":piedata}
    return JsonResponse({"areadata":dic})

