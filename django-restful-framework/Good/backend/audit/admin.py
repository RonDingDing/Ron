from django.contrib import admin

from .models import Order, ProductType, Product, Cost, CostType, Coupon, CouponItem, Member, Unit


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    pass


####################################
class ProductInline(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    pass


####################################

class CostInline(admin.TabularInline):
    model = Cost


class CostAdmin(admin.ModelAdmin):
    pass


class CostTypeAdmin(admin.ModelAdmin):
    inlines = [CostInline]


####################################

class CouponAdmin(admin.ModelAdmin):
    pass


class CouponItemAdmin(admin.ModelAdmin):
    pass


class MemberAdmin(admin.ModelAdmin):
    pass


class UnitAdmin(admin.ModelAdmin):
    pass


model_tuple = (
    (Order, OrderAdmin),
    (ProductType, ProductTypeAdmin),
    (Product, ProductAdmin),
    (Cost, CostAdmin),
    (CostType, CostTypeAdmin),
    (Coupon, CouponAdmin),
    (CouponItem, CouponItemAdmin),
    (Member, MemberAdmin),
    (Unit, UnitAdmin)
)

for original, adminized in model_tuple:
    admin.site.register(original, adminized)
