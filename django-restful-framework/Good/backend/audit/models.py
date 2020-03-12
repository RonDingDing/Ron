from datetime import datetime

from django.db import models


# Create your models here.
def change_time_to_local(datetimeobj: datetime):
    # beijing = timezone(settings.TIME_ZONE)
    local_datetime = datetimeobj
    fmt = '%Y-%m-%d %H:%M:%S'
    return local_datetime.strftime(fmt)

class ProductType(models.Model):
    """产品类型"""
    name = models.CharField(max_length=50, default="无", verbose_name='产品类型')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '产品类型'

def default_product_type():
    return ProductType.objects.get_or_create(name='无', id=0)[0]

# @receiver(class_prepared, sender = ProductType)
# def class_prepare_product_type_receiver(sender, instance, *args, **kwargs):
#     default_product_type()



class Product(models.Model):
    """产品"""
    name = models.CharField(max_length=200, verbose_name='名称')
    _price = models.IntegerField(default=0, verbose_name='价格')
    types = models.ForeignKey(ProductType, on_delete=models.SET(default_product_type), verbose_name='产品类型')
    insert_time = models.DateTimeField(auto_now_add=True, verbose_name='插入时间')
    old = models.BooleanField(default=False, verbose_name='是否旧价格')

    def __str__(self):
        return f'{self.pk}号{self.name} {str(self.price)}元'

    @property
    def price(self):
        return self._price / 100

    @price.setter
    def price(self, val):
        self._price = val * 100

    class Meta:
        verbose_name = verbose_name_plural = '产品'

def default_product():
    return Product.objects.get_or_create(name='无', _price=0, types=default_product_type(), old=True, id=0)[0]

# @receiver(class_prepared, sender = Product)
# def class_prepare_product_receiver(sender, instance, *args, **kwargs):
#     default_product()



# @receiver(post_save, sender=Product)
# def post_save_product_receiver(sender, instance, *args, **kwargs):
#     if instance.id != 0:
#         for number in range(1, 11):
#             Item.objects.get_or_create(product=instance, number=number)




class Member(models.Model):
    """会员"""
    name = models.CharField(max_length=200, verbose_name='名称', unique=True)
    phone = models.CharField(max_length=200, verbose_name='手机', unique=True)

    def __str__(self):
        return f'姓名: {self.name} 手机: {self.phone}'

    class Meta:
        verbose_name = verbose_name_plural = '会员'

def default_member():
    return Member.objects.get_or_create(name='无', phone='无', id=0)[0]


# @receiver(class_prepared, sender = Member)
# def class_prepare_member_receiver(sender, instance, *args, **kwargs):
#     default_member()



class Order(models.Model):
    """订单"""
    order_id = models.IntegerField(default=0, verbose_name='订单ID')
    product = models.ForeignKey(Product, on_delete=models.SET(default_product), verbose_name='产品')
    number = models.IntegerField(default=0, verbose_name='数量')
    sale_time = models.DateTimeField(auto_now_add=True, verbose_name='销售时间' )
    state = models.IntegerField(choices=[(0, "未结清"), (1, "已结清")], default=1)
    discount = models.FloatField(verbose_name='折扣', default=1)
    member = models.ForeignKey(Member, on_delete=models.SET(default_member), verbose_name='会员')

    def __str__(self):
        return f'ID: {self.order_id} 会员:{self.member.name} 总价: {self.product.id}号{self.product.name} * {self.number} = {self.product._price * self.number / 100} 元'

    class Meta:
        verbose_name = verbose_name_plural = '订单'

    @property
    def revenue(self):
        return self.product._price * self.number * self.discount / 100

class CostType(models.Model):
    """成本类型"""
    name = models.CharField(max_length=50, verbose_name='成本类型')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '成本类型'


def default_costtype():
    return CostType.objects.get_or_create(name='无', id=0)[0]

# @receiver(class_prepared, sender = CostType)
# def class_prepare_costtype_receiver(sender, instance, *args, **kwargs):
#     default_costtype()


class Unit(models.Model):
    """单位"""
    name = models.CharField(max_length=50, verbose_name='单位')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '单位'

def default_unit():
    return Unit.objects.get_or_create(name='无', id=0)[0]

# @receiver(class_prepared, sender = Unit)
# def class_prepare_unit_receiver(sender, instance, *args, **kwargs):
#     default_unit()




class Cost(models.Model):
    """成本"""
    name = models.CharField(max_length=200, verbose_name='名称', default='')
    costtype = models.ForeignKey(CostType, on_delete=models.SET(default_costtype), verbose_name='成本类型')
    number = models.FloatField(default=0, verbose_name='数量')
    source = models.TextField(verbose_name='来源')
    unit = models.ForeignKey(Unit, on_delete=models.SET(default_unit), verbose_name='单位')
    _price = models.IntegerField(default=0, verbose_name='价格')
    buy_time = models.DateTimeField(auto_now_add=True, verbose_name='购买时间' )
    state = models.IntegerField(choices=[(0, "未结清"), (1, "已结清")], default=1, verbose_name='状态')

    @property
    def price(self):
        return self._price / 100

    @price.setter
    def price(self, val):
        self._price = val * 100

    @property
    def single_price(self):
        return self._price / 100 / self.number

    class Meta:
        verbose_name = verbose_name_plural = '成本'

    def __str__(self):
        return f'物品: {self.name} 类型: {self.costtype.name} 数量: {self.number} 总价: {self.price} 单价: {self.single_price:.2f} 时间: {change_time_to_local(self.buy_time)}'

class CouponItem(models.Model):
    """优惠券类型"""
    name = models.CharField(max_length=200, verbose_name='名称', default='')


    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = verbose_name_plural = '优惠券类型'

def default_coupon_item():
    return CouponItem.objects.get_or_create(name='无', id=0)[0]


class Coupon(models.Model):
    """优惠券"""
    user = models.ForeignKey(Member, on_delete=models.SET(default_member), verbose_name='用户')
    coupon = models.ForeignKey(CouponItem, on_delete=models.SET(default_coupon_item), verbose_name='优惠券')
    number = models.IntegerField(default=0, verbose_name='数量')
    exchange = models.IntegerField(default=0, verbose_name='兑换次数')

    def __str__(self):
        return f'用户: {self.user.name} 手机: {self.user.phone}  优惠券: {self.coupon.name} * {self.number} 兑换: {self.exchange}'

    class Meta:
        verbose_name = verbose_name_plural = '优惠券'
