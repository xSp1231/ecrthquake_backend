import http
import json
from django.http import JsonResponse
from datamanage.models import Province_eqnum, Province_intro, Provine_magnitude, cluserData, searchAreaData, \
    predictionData


# 发送词云图对应的折线图的数据
def getprovincedata(request):
    name = request.GET.get('province')
    print("省份为 ", name)
    data = Province_eqnum.objects.filter(province=name).first()
    ydata = [data.num2013, data.num2014, data.num2015, data.num2016, data.num2017, data.num2018, data.num2019,
             data.num2020, data.num2021, data.num2022]
    print("ydata is ", ydata)
    return JsonResponse({"ydata": ydata})


# 发送各个省份地震情况简介
def getprovinceintro(request):
    area = request.GET.get('area')
    data = Province_intro.objects.get(province=area)
    piedata = json.loads(data.pie_json)
    for it in piedata:  # 更改键的名字
        it["name"] = it.pop("area")
    dic = {"areaname": data.province, "injure": data.injurenum, "death": data.deathnum, "total": data.total,
           "intro": data.intro, "piedata": piedata, "img": str(data.image)}
    print("dic is ", dic)
    return JsonResponse({"areadata": dic})


# 发送各省份震级数据
def getmagnitudedata(request):
    data = Provine_magnitude.objects.all()
    x = []
    minn = []
    averge = []
    maxx = []
    for it in data:
        x.append(it.province)
        minn.append(it.minn)
        averge.append(it.averge)
        maxx.append(it.maxx)
    return JsonResponse([x, minn, averge, maxx], safe=False)


def getclusterdata(request):
    data = cluserData.objects.all()
    res = []
    for i in data:
        temp = [i.deepth, i.grade, i.cluster]
        res.append(temp)
    return JsonResponse({"data": res}, safe=True)


def getSearchAreaTableData(request):  # get请求
    name = request.GET.get("areaname")
    data = searchAreaData.objects.filter(position__icontains=name)  # 对name 进行模糊查询  name 为子序列
    res = []
    for it in data:
        temp = {"position": it.position, "time": it.date, "magnitude": it.magnitude, "tag": it.tag}
        res.append(temp)
    return JsonResponse({"areaTableData": res}, safe=True)


def getPredictionData(request):  # get请求
    name = request.GET.get("areaname")
    data = predictionData.objects.filter(position__icontains=name)  # 对name 进行模糊查询  name 为子序列
    res = []
    for it in data:
        temp = [it.date, it.magnitude]
        res.append(temp)
    return JsonResponse({"predictionData": res}, safe=True)
