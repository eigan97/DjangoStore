"""TiendaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from tienda.views import index, all_products,all_categoriaA,all_productsA,add_product_submit,add_categorias_submit, eliminar_producto, editar_producto, eliminar_categoria, editar_categoria,venta
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('home/',index,name='home'),
    path('productos/',all_products,name='productos'),
    path('administracion/categorias/',all_categoriaA,name='adminCategorias'),
    path('administracion/productos/',all_productsA,name='adminpPoductos'),
    path('administracion/productos/add/submit',add_product_submit,name='add_product_submit'),
    path('administracion/categorias/add/submit',add_categorias_submit,name='add_categorias_submit'),
    path('eliminar/producto/<id_producto>',eliminar_producto,name='eliminar_producto'),
    path('editar/producto/<id_producto>',editar_producto,name='editar_producto'),
    path('eliminar/categoria/<id_categoria>',eliminar_categoria,name='eliminar_categoria'),
    path('editar/categoria/<id_categoria>',editar_categoria,name='editar_categoria'),
    path('venta/',venta,name='venta')
]
