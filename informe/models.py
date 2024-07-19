from django.db import models

class Informe(models.Model):
    id_inf_tec = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE, db_column='idCliente')
    id_mecanico = models.ForeignKey('Mecanico',on_delete=models.CASCADE, db_column='idMecanico')
    orden_servicio = models.CharField(max_length=100)
    trabajo_solicitado = models.TextField(null=True, blank=True)
    trabajos_realizados = models.TextField(null=True, blank=True)
    evaluacion = models.TextField(null=True, blank=True)
    enlaces_fotos = models.URLField(blank=True, null=True)
    enlaces_videos = models.URLField(blank=True, null=True)
    conclusion = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id_inf_tec)
    
class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='idCliente', primary_key=True)
    nombre_empresa = models.CharField(max_length=20)
    nombre_cliente = models.CharField(max_length=20)
    cli_apellido_paterno = models.CharField(max_length=20)
    cli_apellido_materno = models.CharField(max_length=20)
    numero_celular = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id_cliente) 
    
class Mecanico(models.Model):
    id_mecanico = models.AutoField(db_column='idMecanico', primary_key=True)
    nombre_mecanico = models.CharField(max_length=20)
    mec_apellido_paterno = models.CharField(max_length=20)
    mec_apellido_materno = models.CharField(max_length=20)
    numero_celular = models.CharField(max_length=45)
    id_cargo = models.ForeignKey('Cargo',on_delete=models.CASCADE, db_column='idCargo')

    def __str__(self):
        return str(self.id_mecanico)
    
class Cargo(models.Model):
    id_cargo = models.AutoField(db_column='idCargo', primary_key=True)
    nombre_cargo = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_cargo)
    

class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=60)
    rut_cliente = models.CharField(max_length=15)
    direccion_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=20)
    correo_cliente = models.EmailField()
    año_vehiculo = models.PositiveIntegerField()
    marca_vehiculo = models.CharField(max_length=20)
    modelo_vehiculo = models.CharField(max_length=20)
    trabajo_solicitado = models.TextField()
    respaldo_fotografico = models.URLField()
    observaciones = models.TextField()

    def __str__(self):
        return str(self.nombre_cliente)
    

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    correo_electrónico = models.EmailField()

    def __str__(self):
        return str(self.nombre)





