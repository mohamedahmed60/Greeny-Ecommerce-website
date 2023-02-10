from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail , CategoryList ,post_list

app_name = 'products'
urlpatterns = [
    path('test', post_list),
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_details'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandDetail.as_view(), name='brand_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),


]
