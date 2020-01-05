from audit.revenue.views import RevenueVueSet
from django.urls import path, register_converter
from audit.converters import DateTimeConverter, NumberListConverter

revenue_create = RevenueVueSet.as_view({'get': 'create'})

register_converter(DateTimeConverter, 'datetime')
register_converter(NumberListConverter, 'numlist')

urlpatterns = [
    path('create/<numlist:nums>/', revenue_create, name='revenue.revenue_create')

]
