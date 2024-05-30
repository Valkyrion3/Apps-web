# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categorias', views.categorias, name='categorias'),
    path('piezas', views.piezas, name='piezas'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('suministros', views.suministros, name='suministros'),
    path('detalles', views.detalles, name='detalles'),
    path('', views.pagina_principal, name='inicio'),  # URL raíz
    path('home', views.pagina_principal, name='home'),  # URL raíz
    path('categorias/agregar', views.agregar_categoria, name='agregar_categoria'),
    path('piezas/agregar', views.agregar_pieza, name='agregar_pieza'),
    path('proveedor/agregar', views.agregar_proveedor, name='agregar_proveedor'),
    path('suministro/agregar', views.agregar_suministro, name='agregar_suministro'),
    path('detalle/agregar', views.agregar_detalle, name='agregar_detalle'),
    #Actualziar y Eliminar
    path('categoria/actualizar/<int:id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    #Piezas
    path('pieza/actualizar/<int:id>/', views.actualizar_pieza, name='actualizar_pieza'),
    path('pieza/eliminar/<int:id>/', views.eliminar_pieza, name='eliminar_pieza'),
    #Proveedores
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    #Suministros
    path('suministro/actualizar/<int:id>/', views.actualizar_suministro, name='actualizar_suministro'),
    path('suministro/eliminar/<int:id>/', views.eliminar_suministro, name='eliminar_suministro'),
    #Detalles
    path('detalle/actualizar/<int:id>/', views.actualizar_detalle, name='actualizar_detalle'),
    path('detalle/eliminar/<int:id>/', views.eliminar_detalle, name='eliminar_detalle'),
]
