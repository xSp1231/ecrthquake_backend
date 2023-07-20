import http
import json
from django.http import JsonResponse
from datamanage.models import Province_eqnum, Province_intro, Provine_magnitude, cluserData, searchAreaData, \
    predictionData, doubleBarMagnitude, pieData


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


# 发送双重柱状图里面的震级 震深数据
def getDoubleBarData(request):
    name = request.GET.get("areaname")
    data = doubleBarMagnitude.objects.get(position__icontains=name)  # 模糊查询
    # 弱中强震级数据
    magnitudeData = [data.sMagnitude, data.mMagnitude, data.lMagnitude]
    # 弱中强震源深度数据
    depthData = [data.sDepth, data.mDepth, data.lDepth]
    return JsonResponse({"flag": True, "magnitudeData": magnitudeData, "depthData": depthData}, safe=True)


# 获取饼图里面的数据 根据前端传来的数据  (地名,数据类型) 新疆皮山县 弱震级
def getPidData(request):
    from collections import Counter
    name = request.GET.get("areaname")
    kind = request.GET.get("kind")
    print("name is ", name)
    print("kind is ", kind)
    res = []
    ans = []
    if "震级" in kind:  # 如果是震级数据       "新疆皮山  弱震级"
        data = pieData.objects.filter(position__icontains=name, magnitudeTag=kind)
        for it in data:
            res.append(it.magnitude)
        count_dict = Counter(res)
        # 输出统计结果
        count_dict = dict(count_dict)  # 转为字典
        for it in count_dict.items():
            ans.append({"value": it[1], "name": it[0]})
        # print("震级饼图数据", ans)
        # print("图标数组", list(count_dict.keys()))
        return JsonResponse({"flag": "震级数据", "pieData": ans, "legend": list(count_dict.keys())})
    elif "震深" in kind:  # 如果是震深数据       "新疆皮山  弱震深"
        data = pieData.objects.filter(position__icontains=name, depthTag=kind)  # 检查名字 与震深标签
        for it in data:
            res.append(it.depth)
        count_dict = Counter(res)
        count_dict = dict(count_dict)  # 转为字典
        for it in count_dict.items():
            ans.append({"value": it[1], "name": it[0]})
        return JsonResponse({"flag": "震深数据", "pieData": ans, "legend": list(count_dict.keys())})
