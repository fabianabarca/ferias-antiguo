from django.urls import path

from . import views

urlpatterns = [
    path('', views.ferias, name='list-ferias'),
    path('lista/',
         views.lista_productos, name='lista-productos'),
    path('<str:feria_id>/',
         views.ferias_detail, name='feria-detail'),
    path('<str:feria_id>/<slug:slug>/', 
         views.ferias_detail, name='feria-detail'),
]
