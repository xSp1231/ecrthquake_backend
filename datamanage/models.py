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

class Province_intro(models.Model):
    province = models.CharField(max_length=10, verbose_name='省份')
    deathnum=models.IntegerField(verbose_name='受伤人数')
    injurenum=models.IntegerField(verbose_name='死亡人数')
    total=models.IntegerField(verbose_name='伤亡人数')
    intro=models.CharField(max_length=100,verbose_name='省份地理简介')
    pie_json=models.CharField(max_length=600,verbose_name='饼图数据')
    class Meta:
        db_table = "province_intro"  # 修改数据表的名字

