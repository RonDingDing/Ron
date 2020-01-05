from audit.management.views import CostTypeViewSet, ProducttypeViewSet, ProductViewSet
from django.urls import path, register_converter
from audit.converters import FloatConverter

register_converter(FloatConverter, 'float')

costtype_create = CostTypeViewSet.as_view({'get': 'create'})
costtype_list = CostTypeViewSet.as_view({'get': 'list'})

producttype_create = ProducttypeViewSet.as_view({'get': 'create'})
producttype_list = ProducttypeViewSet.as_view({'get': 'list'})

product_create = ProductViewSet.as_view({'get': 'create'})
product_list = ProductViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('costtype/create/<str:name>/', costtype_create, name='management.costtype_create'),
    path('costtype/list/', costtype_list, name='management.costtype_list'),

    path('producttype/create/<str:name>/', producttype_create, name='management.producttype_create'),
    path('producttype/list/', producttype_list, name='management.producttype_list'),

    path('product/create/<str:name>/<float:price>/<int:types>/', product_create, name='management.product_create'),
    path('product/list/', product_list, name='management.product_list'),
]
