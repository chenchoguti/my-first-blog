from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.listar_pub, name='listar_pub'),
    path('pub/<int:pk>/', views.pub_detail, name='pub_detail'),
]