from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:id_contato>/', views.detalhes, name='detalhes'),
    path('novo/', views.novo_contato, name='novo')
]



