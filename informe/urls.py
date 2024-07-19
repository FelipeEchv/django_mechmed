from django.urls import path, include
from . import views
from .views import buscar_informes

urlpatterns = [
    path('', views.portada, name='portada'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('buscar_informes/', buscar_informes, name='buscar_informes'),

    path('menu', views.index, name='index'),

    path('informes/', views.lista_informes, name='lista_informes'),
    path('informes/crear/', views.crear_informe, name='crear_informe'),
    path('informes/visualizar/<int:id_inf_tec>/', views.visualizar_informe, name='visualizar_informe'),
    path('informes/editar/<int:id_inf_tec>/', views.editar_informe, name='editar_informe'),
    path('informes/eliminar/<int:id_inf_tec>/', views.eliminar_informe, name='eliminar_informe'),

    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<int:id_cliente>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id_cliente>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    path('mecanicos/', views.lista_mecanicos, name='lista_mecanicos'),
    path('mecanicos/crear/', views.crear_mecanico, name='crear_mecanico'),
    path('mecanicos/<int:id_mecanico>/editar/', views.editar_mecanico, name='editar_mecanico'),
    path('mecanicos/<int:id_mecanico>/eliminar/', views.eliminar_mecanico, name='eliminar_mecanico'),

    path('cargos/', views.lista_cargos, name='lista_cargos'),
    path('cargos/crear/', views.crear_cargo, name='crear_cargo'),
    path('cargos/<int:id_cargo>/editar/', views.editar_cargo, name='editar_cargo'),
    path('cargos/<int:id_cargo>/eliminar/', views.eliminar_cargo, name='eliminar_cargo'),


    path('usuarios/', views.usuarios, name='usuarios'),
    path("accounts/", include("django.contrib.auth.urls")),


    path('presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
    path('presupuestos/crear/', views.crear_presupuesto, name='crear_presupuesto'),
    path('presupuestos/<int:pk>/editar/', views.editar_presupuesto, name='editar_presupuesto'),
    path('presupuestos/<int:pk>/eliminar/', views.eliminar_presupuesto, name='eliminar_presupuesto'),
    path('presupuestos/<int:pk>/', views.ver_presupuesto, name='ver_presupuesto'),



    path('crear_solicitud/', views.crear_solicitud, name='crear_solicitud'),
    path('lista_solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('eliminar_solicitud/<int:solicitud_id>/', views.eliminar_solicitud, name='eliminar_solicitud'),
]
