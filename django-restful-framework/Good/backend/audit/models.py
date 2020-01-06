import time

from django.db import models


# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50, default="无", verbose_name='类别')

    def __str__(self):
        return self.name


def default_product_type():
    return ProductType.objects.get_or_create(name='无', pk=0)[0]

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='名称')
    _price = models.IntegerField(default=0, verbose_name='价格')
    types = models.ForeignKey(ProductType, on_delete=models.SET(default_product_type), default=0, verbose_name='类别')
    insert_time = models.DateTimeField(auto_now_add=True, verbose_name='插入时间' )
    old = models.BooleanField(default=False, verbose_name='是否旧价格')

    def __str__(self):
        return ', '.join([self.name, str(self.price)])

    @property
    def price(self):
        return self._price / 100

    @price.setter
    def price(self, val):
        self._price = val


class Order(models.Model):
    products = models.ManyToManyField(Product, verbose_name='产品')
    sale_time = models.DateTimeField(auto_now_add=True, verbose_name='销售时间' )
    state = models.IntegerField(choices=[(0, "未结清"), (1, "已结清")], default=1)
    revenue = models.FloatField(verbose_name='收入')


class CostType(models.Model):
    name = models.CharField(max_length=50, verbose_name='类别')

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50, verbose_name='单位')

    def __str__(self):
        return self.name

class Cost(models.Model):
    costtype = models.ForeignKey(CostType, on_delete=models.SET(default_product_type), default=0, verbose_name='成本类型')
    number = models.FloatField(default=0, verbose_name='数量')
    source = models.TextField(verbose_name='来源')
    unit = models.ForeignKey(Unit, on_delete=models.SET(default_product_type), default=0, verbose_name='单位')
    single_price = models.FloatField(default=0, verbose_name='单价')
    _price = models.IntegerField(default=0, verbose_name='价格')
    buy_time = models.DateTimeField(auto_now_add=True, verbose_name='购买时间' )
    state = models.IntegerField(choices=[(0, "未结清"), (1, "已结清")], default=1, verbose_name='状态')

    @property
    def price(self):
        return self._price / 100
