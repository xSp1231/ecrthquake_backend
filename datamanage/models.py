from django.db import models


# 每个省份每一年的地震次数
class Province_eqnum(models.Model):
    province = models.CharField(max_length=10, verbose_name='省份')
    num2013 = models.IntegerField(verbose_name='2013')
    num2014 = models.IntegerField(verbose_name='2014')
    num2015 = models.IntegerField(verbose_name='2015')
    num2016 = models.IntegerField(verbose_name='2016')
    num2017 = models.IntegerField(verbose_name='2017')
    num2018 = models.IntegerField(verbose_name='2018')
    num2019 = models.IntegerField(verbose_name='2019')
    num2020 = models.IntegerField(verbose_name='2020')
    num2021 = models.IntegerField(verbose_name='2021')
    num2022 = models.IntegerField(verbose_name='2022')

    class Meta:
        db_table = "province_eqnum_year"  # 修改数据表的名字


# 添加模型类
class Province_intro(models.Model):
    province = models.CharField(max_length=10, verbose_name='省份')
    deathnum = models.IntegerField(verbose_name='受伤人数')
    injurenum = models.IntegerField(verbose_name='死亡人数')
    total = models.IntegerField(verbose_name='伤亡人数', null=True)
    intro = models.CharField(max_length=100, verbose_name='省份地理简介')
    pie_json = models.CharField(max_length=600, verbose_name='饼图数据')
    image = models.ImageField(upload_to='pictures/', default='pictures/default.jpg')

    class Meta:
        db_table = "province_intro"  # 修改数据表的名字


class Provine_magnitude(models.Model):
    province = models.CharField(max_length=10, verbose_name='省份')
    minn = models.FloatField()
    averge = models.FloatField()
    maxx = models.FloatField()
    f = models.FloatField(default=0)  # 强震频率

    class Meta:
        db_table = "province_magnitude"  # 修改数据表的名字


class cluserData(models.Model):
    deepth = models.FloatField()
    grade = models.FloatField()
    cluster = models.IntegerField()

    class Meta:
        db_table = "clusterData"  # 修改数据表的名字


# 搜索选项里面的地区数据
class searchAreaData(models.Model):
    position = models.CharField(max_length=20)  # 地点
    date = models.DateField()  # 时间
    magnitude = models.FloatField()  # 震级
    tag = models.CharField(max_length=20)  # 标签

    class Meta:
        db_table = "searchAreaData"  # 修改数据表的名字


class predictionData(models.Model):
    position = models.CharField(max_length=20)  # 地点
    date = models.DateField()  # 时间
    magnitude = models.FloatField()  # 震级

    class Meta:
        db_table = "predictionData"  # 修改数据表的名字


class doubleBarMagnitude(models.Model):
    position = models.CharField(max_length=20)  # 地点
    sMagnitude = models.FloatField()  # 弱震级
    mMagnitude = models.FloatField()  # 中震级
    lMagnitude = models.FloatField()  # 强震级
    sDepth = models.FloatField()  # 弱震深
    mDepth = models.FloatField()  # 中震深
    lDepth = models.FloatField()  # 强震深

    class Meta:
        db_table = "doubleBarData"  # 修改数据表的名字


class pieData(models.Model): #与双轴柱状图关联的饼图的数据
    position = models.CharField(max_length=20)  # 地点
    depth = models.FloatField()  # 震深
    magnitude = models.FloatField()  # 震级
    magnitudeTag=models.CharField(max_length=10) # 震级标签
    depthTag=models.CharField(max_length=10) # 震源标签

    class Meta:
        db_table = "pieData"  # 修改数据表的名字
