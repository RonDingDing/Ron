from django.db import models
import time


# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=200, default="无")


def default_product_type():
    return ProductType.objects.get_or_create(name='无', pk=0)[0]


class Product(models.Model):
    name = models.CharField(max_length=200)
    _price = models.IntegerField(default=0)
    types = models.ForeignKey(ProductType, on_delete=models.SET(default_product_type), default=0)
    insert_time = models.IntegerField(default=int(time.time()))
    old = models.BooleanField(default=False)

    @property
    def price(self):
        return self._price / 100

    @price.setter
    def price(self, val):
        self._price = val


class Order(models.Model):
    products = models.ManyToManyField(Product)
    sale_time = models.IntegerField(default=time.time)
    state = models.IntegerField(choices=[(0, "未结清"), (1, "已结清")])


class CostType(models.Model):
    name = models.CharField(max_length=200)


class Cost(models.Model):
    item = models.ManyToManyField(CostType)
    _price = models.IntegerField(default=0)
    buy_time = models.IntegerField(default=time.time)
    state = models.IntegerField(choices=[(0, "未结清"), (1, "已结清")])

    @property
    def price(self):
        return self._price / 100
