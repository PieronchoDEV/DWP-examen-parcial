from django.urls import path
from . import views # . significa directorio local

app_name='gestionTienda'

urlpatterns =[
    path('',views.index,name='index'),
    path('Productos',views.productos,name='productos'),
    path('eliminarProducto/<str:idProducto>',views.eliminarProducto,name='eliminarProducto'),
    path('eliminarTienda/<str:idTienda>',views.eliminarTienda,name='eliminarTienda'),
    path('asignarTienda',views.asignarTienda,name='asignarTienda'),
    path('detalleTienda/<str:idTienda>',views.detalleTienda,name='detalleTienda'),
     
]


