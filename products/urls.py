from django.urls import path
from .views import ProductList

appname='products'
urlpatterns = [
    path('', ProductList.as_view(), name='product_list')
]
