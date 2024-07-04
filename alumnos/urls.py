# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('carrito/', views.carrito, name='carrito'),  
    path('productos/', views.productos, name='productos'),
    path('descpolera1/', views.descpolera1, name='descpolera1'),
    path('descpolera2/', views.descpolera2, name='descpolera2'),
    path('descpolera3/', views.descpolera3, name='descpolera3'),
    path('descpolera4/', views.descpolera4, name='descpolera4'),
    path('descpolera5/', views.descpolera5, name='descpolera5'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('envios/', views.envios, name='envios'),
    path('devolucion/', views.devolucion, name='devolucion'),
    path('pago/', views.pago, name='pago'),
]
