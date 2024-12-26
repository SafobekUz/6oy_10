from django.urls import path
from . import views

urlpatterns = [
    path('flowers/', views.all_flowers, name='all_flowers'),
    path('flowers/type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),
    path('flowers/<int:flower_id>/', views.single_flower, name='single_flower'),
    path('tur/<int:tur_id>/update/', views.update_tur, name='update_tur'),
    path('gul/<int:gul_id>/update/', views.update_gul, name='update_gul'),
]
