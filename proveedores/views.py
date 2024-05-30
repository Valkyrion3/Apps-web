from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *

#Pagina principal
def pagina_principal(request):
    return render(request, 'home.html')
#listar categorias
def categorias(request):
    categorias = categoria.objects.all()
    context = {'categorias':categorias}
    return render(request, 'categorias/categorias.html', context)
#agregar categorias
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/agregar.html', {'form': form})
#listar piezas
def piezas(request):
    piezas = pieza.objects.all()
    context = {'piezas':piezas}
    # Lógica para obtener y mostrar las piezas
    return render(request, 'piezas/piezas.html', context)
#agregar piezas
def agregar_pieza(request):
    if request.method == 'POST':
        form = PiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('piezas')
    else:
        form = PiezaForm()
    return render(request, 'piezas/agregar.html', {'form': form})
#listar proveedores
def proveedores(request):
    proveedores = proveedor.objects.all()
    context = {'proveedores':proveedores}
    # Lógica para obtener y mostrar los proveedores
    return render(request, 'proveedores/proveedores.html', context)
#Agregar proveedores
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/agregar.html', {'form': form})
#Listar suministros
def suministros(request):
    suministros = suministro.objects.all()
    context = {'suministros':suministros}
    # Lógica para obtener y mostrar los suministros
    return render(request, 'suministros/suministros.html', context)
#Agregar suministros
def agregar_suministro(request):
    if request.method == 'POST':
        form = SuministroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suministros')
    else:
        form = SuministroForm()
    return render(request, 'suministros/agregar.html', {'form': form})
#listar detalles
def detalles(request):
    detalles = suministro_pieza.objects.all()
    context = {'detalles':detalles}
    return render(request, 'detalle/detalle.html', context)
#Agregar detalles
def agregar_detalle(request):
    if request.method == 'POST':
        form = DetallesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalles')
    else:
        form = DetallesForm()
    return render(request, 'detalle/agregar.html', {'form': form})
#Eliminar
#Categorias
def eliminar_categoria(request,id):
    categori = get_object_or_404(categoria, id=id)  # Obtiene el cliente a eliminar
    if request.method == 'POST':  # Si se envía el formulario
        categori.delete()  # Elimina el cliente de la base de datos
        return redirect('categorias')  # Redirige a la lista de clientes
    return render(request, 'categorias.html', {'categorias': categoria}) 
#Piezas
def eliminar_pieza(request,id):
    categori = get_object_or_404(pieza, id=id)  # Obtiene el cliente a eliminar
    if request.method == 'POST':  # Si se envía el formulario
        categori.delete()  # Elimina el cliente de la base de datos
        return redirect('piezas')  # Redirige a la lista de clientes
    return render(request, 'categorias.html', {'piezas': pieza}) 
#Proveedores
def eliminar_proveedor(request,id):
    categori = get_object_or_404(proveedor, id=id)  # Obtiene el cliente a eliminar
    if request.method == 'POST':  # Si se envía el formulario
        categori.delete()  # Elimina el cliente de la base de datos
        return redirect('proveedores')  # Redirige a la lista de clientes
    return render(request, 'proveedores.html', {'proveedores': proveedor}) 
#Suministros
def eliminar_suministro(request,id):
    categori = get_object_or_404(suministro, id=id)  # Obtiene el cliente a eliminar
    if request.method == 'POST':  # Si se envía el formulario
        categori.delete()  # Elimina el cliente de la base de datos
        return redirect('suministros')  # Redirige a la lista de clientes
    return render(request, 'suministros.html', {'suministros': suministro}) 
#detalles
def eliminar_detalle(request,id):
    categori = get_object_or_404(suministro_pieza, id=id)  # Obtiene el cliente a eliminar
    if request.method == 'POST':  # Si se envía el formulario
        categori.delete()  # Elimina el cliente de la base de datos
        return redirect('detalles')  # Redirige a la lista de clientes
    return render(request, 'detalle.html', {'detalles': suministro_pieza}) 

#Actualizar
#Categorias
def actualizar_categoria(request, id):
    # Obtener la categoría existente
    categori = get_object_or_404(categoria, id=id)
    
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos de la solicitud POST
        form = CategoriaForm(request.POST, instance=categori)
        if form.is_valid():
            # Guardar los cambios en la categoría
            form.save()
            # Redirigir a la página de listado de categorías
            return redirect('categorias')
    else:
        # Crear una instancia del formulario con los datos de la categoría existente
        form = CategoriaForm(instance=categori)
    
    # Renderizar la plantilla con el formulario
    return render(request, 'categorias/actualizar.html', {'form': form})
#Pieza
def actualizar_pieza(request,id):
    categori = get_object_or_404(pieza, id=id)
    if request.method == 'POST':
        form = PiezaForm(request.POST, instance=categori)
        if form.is_valid():
            form.save()
            return redirect('piezas')
    else:
        form = PiezaForm(instance=categori)
    return render(request, 'piezas/actualizar.html', {'form': form})
#Proveedores
def actualizar_proveedor(request,id):
    categori = get_object_or_404(proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=categori)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=categori)
    return render(request, 'proveedores/actualizar.html', {'form': form})
#suministro
def actualizar_suministro(request,id):
    categori = get_object_or_404(suministro, id=id)
    if request.method == 'POST':
        form = SuministroForm(request.POST, instance=categori)
        if form.is_valid():
            form.save()
            return redirect('suministros')
    else:
        form = SuministroForm(instance=categori)
    return render(request, 'suministros/actualizar.html', {'form': form})
#detalle
def actualizar_detalle(request,id):
    categori = get_object_or_404(suministro_pieza, id=id)
    if request.method == 'POST':
        form = DetallesForm(request.POST, instance=categori)
        if form.is_valid():
            form.save()
            return redirect('detalles')
    else:
        form = DetallesForm(instance=categori)
    return render(request, 'detalle/actualizar.html', {'form': form})