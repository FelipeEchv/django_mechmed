from django.contrib import admin
from .models import Informe, Cliente, Mecanico, Cargo, Presupuesto, Solicitud


admin.site.register(Informe)
admin.site.register(Cliente)
admin.site.register(Mecanico)
admin.site.register(Cargo)
admin.site.register(Presupuesto)
admin.site.register(Solicitud)

