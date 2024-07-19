from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Informe, Cliente, Mecanico, Cargo, Presupuesto, Solicitud
from .forms import InformeForm, ClienteForm, MecanicoForm, CargoForm, PresupuestoForm, SolicitudForm

from django.shortcuts import render

def portada(request):
    return render(request, 'informe/portada.html')

def servicios(request):
    return render(request, 'informe/servicios.html')

def nosotros(request):
    return render(request, 'informe/nosotros.html')

def contacto(request):
    return render(request, 'informe/contacto.html')

def login_view(request):
    return render(request, 'informe/login.html')

def buscar_informe(request):
    return render(request, 'informe/buscar_informe.html')

#------------------------------------
@login_required 
def index(request):
    request.session["usuario"]="CarlosF."
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'informe/index.html',context)

@login_required 
def informes(request):
    return render(request, 'informe/lista_informes.html')

@login_required 
def usuarios(request):
    return render(request, 'informe/usuarios.html')

@login_required 
def crear_informe(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_informes')
    else:
        form = InformeForm()
    return render(request, 'informe/crear_informe.html', {'form': form})

@login_required 
def editar_informe(request, id_inf_tec):
    informe = get_object_or_404(Informe, id_inf_tec=id_inf_tec)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        if form.is_valid():
            form.save()
            return redirect('lista_informes')
    else:
        form = InformeForm(instance=informe)
    return render(request, 'informe/editar_informe.html', {'form': form})
    
@login_required
def eliminar_informe(request, id_inf_tec):
    informe = get_object_or_404(Informe, id_inf_tec=id_inf_tec)
    if request.method == 'POST':
        informe.delete()
        return redirect('lista_informes')
    return render(request, 'informe/eliminar_informe.html', {'informe': informe})

@login_required
def lista_informes(request):
    informes = Informe.objects.all()
    return render(request, 'informe/lista_informes.html', {'informes': informes})

@login_required
def visualizar_informe(request, id_inf_tec):
    informe = get_object_or_404(Informe, id_inf_tec=id_inf_tec)
    return render(request, 'informe/visualizar_informe.html', {'informe': informe})

#clientes
@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'informe/crear_cliente.html', {'form': form})

@login_required
def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'informe/editar_cliente.html', {'form': form})

@login_required
def eliminar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'informe/eliminar_cliente.html', {'cliente': cliente})

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'informe/lista_clientes.html', {'clientes': clientes})

#mecanicos
@login_required
def crear_mecanico(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mecanicos')
    else:
        form = MecanicoForm()
    return render(request, 'informe/crear_mecanico.html', {'form': form})

@login_required
def editar_mecanico(request, id_mecanico):
    mecanico = get_object_or_404(Mecanico, id_mecanico=id_mecanico)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('lista_mecanicos')
    else:
        form = MecanicoForm(instance=mecanico)
    return render(request, 'informe/editar_mecanico.html', {'form': form})

@login_required
def eliminar_mecanico(request, id_mecanico):
    mecanico = get_object_or_404(Mecanico, id_mecanico=id_mecanico)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('lista_mecanicos')
    return render(request, 'informe/eliminar_mecanico.html', {'mecanico': mecanico})

@login_required
def lista_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'informe/lista_mecanicos.html', {'mecanicos': mecanicos})
#cargos
@login_required
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cargos')
    else:
        form = CargoForm()
    return render(request, 'informe/crear_cargo.html', {'form': form})

@login_required
def editar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id_cargo=id_cargo)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('lista_cargos')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'informe/editar_cargo.html', {'form': form})

@login_required
def eliminar_cargo(request, id_cargo):
    cargo = get_object_or_404(Cargo, id_cargo=id_cargo)
    if request.method == 'POST':
        cargo.delete()
        return redirect('lista_cargos')
    return render(request, 'informe/eliminar_cargo.html', {'cargo': cargo})

@login_required
def lista_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'informe/lista_cargos.html', {'cargos': cargos})

#Presupuestos
@login_required
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'informe/lista_presupuestos.html', {'presupuestos': presupuestos})

@login_required
def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_presupuestos')
    else:
        form = PresupuestoForm()
    return render(request, 'informe/crear_presupuesto.html', {'form': form})

@login_required
def editar_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, request.FILES, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect('lista_presupuestos')
    else:
        form = PresupuestoForm(instance=presupuesto)
    return render(request, 'informe/editar_presupuesto.html', {'form': form})

@login_required
def eliminar_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    if request.method == 'POST':
        presupuesto.delete()
        return redirect('lista_presupuestos')
    return render(request, 'informe/eliminar_presupuesto.html', {'presupuesto': presupuesto})

@login_required
def ver_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    return render(request, 'informe/ver_presupuesto.html', {'presupuesto': presupuesto})


def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portada')  
    else:
        form = SolicitudForm()
    return render(request, 'informe/solicitud_form.html', {'form': form})

@login_required
def lista_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'informe/lista_solicitudes.html', {'solicitudes': solicitudes})

@login_required
def eliminar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id_solicitud=solicitud_id)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('lista_solicitudes')
    return render(request, 'informe/confirmar_eliminar.html', {'solicitud': solicitud})

#buscar_informes
def buscar_informes(request):
    informe = None
    mensaje_error = ''

    if request.method == 'GET':
        id_inf_tec = request.GET.get('id_inf_tec')
        rut_cliente = request.GET.get('rut_cliente')

        if id_inf_tec or rut_cliente:
            if id_inf_tec:
                try:
                    informe = Informe.objects.get(id_inf_tec=id_inf_tec)
                except Informe.DoesNotExist:
                    mensaje_error = 'Informe no encontrado.'
            elif rut_cliente:
                try:
                    cliente = Cliente.objects.get(numero_celular=rut_cliente)
                    informe = Informe.objects.filter(id_cliente=cliente).first()
                    if not informe:
                        mensaje_error = 'No se encontraron informes para el cliente con el RUT proporcionado.'
                except Cliente.DoesNotExist:
                    mensaje_error = 'Cliente no encontrado.'
    return render(request, 'buscar_informes.html', {'informe': informe, 'mensaje_error': mensaje_error})
