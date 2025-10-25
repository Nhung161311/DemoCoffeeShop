from django.urls import path
from app_shop.views import *

app_name = 'app_shop'
urlpatterns = [
    path('', trang_chu, name='trang_chu'),
    path('gioi-thieu/', gioi_thieu, name='gioi_thieu'),
    path('lien-he/', lien_he, name='lien_he'),
    path('danh-muc/<int:danh_muc_id>/', danh_muc, name='danh_muc'),
    path('demo-dtl/', demo_dtl),
    path('dang-ky/', dang_ky, name='dang_ky')
    
]