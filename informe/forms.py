from django import forms
from .models import Informe, Cliente, Mecanico, Cargo, Presupuesto, Solicitud

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = [
            'fecha',
            'id_mecanico',
            'id_cliente',
            'orden_servicio',
            'trabajo_solicitado',
            'trabajos_realizados',
            'evaluacion',
            'enlaces_fotos',
            'enlaces_videos',
            'conclusion'
        ]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre_empresa',
            'nombre_cliente',
            'cli_apellido_paterno',
            'cli_apellido_materno',
            'numero_celular'
        ]

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = [
            'nombre_mecanico',
            'mec_apellido_paterno',
            'mec_apellido_materno',
            'numero_celular',
            'id_cargo'
        ]

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = [
            'nombre_cargo'
        ]

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = [
            'id_presupuesto',
            'nombre_cliente',
            'rut_cliente',
            'direccion_cliente',
            'telefono_cliente',
            'correo_cliente',
            'año_vehiculo',
            'marca_vehiculo',
            'modelo_vehiculo',
            'trabajo_solicitado',
            'respaldo_fotografico',
            'observaciones',
        ]

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'id_solicitud',
            'nombre',
            'telefono',
            'correo_electrónico',
        ]
        
