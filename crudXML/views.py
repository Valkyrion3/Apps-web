# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import XMLFile
from .forms import XMLFileForm, XMLFileEditForm
from .utils import parse_xml_content
from .forms import XMLFileCreateForm
from .forms import XMLFileValueEditForm
import xml.etree.ElementTree as ET
import os
from django.conf import settings
from django.http import FileResponse

def xmlfile_create(request):
    if request.method == 'POST':
        form = XMLFileCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            car_data = {
                'color': form.cleaned_data['color'],
                'textura': form.cleaned_data['textura'],
                'precio': form.cleaned_data['precio'],
                'modelo': form.cleaned_data['modelo'],
                'marca': form.cleaned_data['marca'],
                'potencia': form.cleaned_data['potencia'],
                'vel_max': form.cleaned_data['vel_max'],
                'tipo_transmision': form.cleaned_data['tipo_transmision'],
                'tipo_combustible': form.cleaned_data['tipo_combustible'],
            }
            
            # Crear el XML
            car = ET.Element('car')
            for key, value in car_data.items():
                child = ET.SubElement(car, key)
                child.text = str(value)
            
            # Convertir el XML a una cadena
            xml_content = ET.tostring(car, encoding='unicode')
            
            # Guardar en el modelo
            xmlfile = XMLFile(name=name, content=xml_content)
            xmlfile.save()
            
            return redirect('xmlfile_list')
    else:
        form = XMLFileCreateForm()
    
    return render(request, 'xmlfile_create.html', {'form': form})

def xmlfile_list(request):
    files = XMLFile.objects.all()
    return render(request, 'xmlfile_list.html', {'files': files})

def xmlfile_upload(request):
    if request.method == 'POST':
        form = XMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            xmlfile = form.save()
            xmlfile.content = xmlfile.file.read().decode('utf-8')
            xmlfile.save()
            return redirect('xmlfile_list')
    else:
        form = XMLFileForm()
    return render(request, 'xmlfile_upload.html', {'form': form})

def xmlfile_detail(request, pk):
    file = get_object_or_404(XMLFile, pk=pk)
    car_data = parse_xml_content(file.content)
    return render(request, 'xmlfile_detail.html', {'file': file, 'car_data': car_data})

def xmlfile_edit(request, pk):
    file = get_object_or_404(XMLFile, pk=pk)
    car_data = parse_xml_content(file.content)
    
    if request.method == 'POST':
        form = XMLFileValueEditForm(request.POST)
        if form.is_valid():
            car_data = {
                'color': form.cleaned_data['color'],
                'textura': form.cleaned_data['textura'],
                'precio': form.cleaned_data['precio'],
                'modelo': form.cleaned_data['modelo'],
                'marca': form.cleaned_data['marca'],
                'potencia': form.cleaned_data['potencia'],
                'vel_max': form.cleaned_data['vel_max'],
                'tipo_transmision': form.cleaned_data['tipo_transmision'],
                'tipo_combustible': form.cleaned_data['tipo_combustible'],
            }
            
            # Crear el XML
            car = ET.Element('car')
            for key, value in car_data.items():
                child = ET.SubElement(car, key)
                child.text = str(value)
            
            # Convertir el XML a una cadena
            xml_content = ET.tostring(car, encoding='unicode')
            
            # Actualizar el contenido del archivo
            file.content = xml_content
            file.save()
            
            return redirect('xmlfile_list')
    else:
        form = XMLFileValueEditForm(initial=car_data)
    
    return render(request, 'xmlfile_edit.html', {'form': form, 'file': file})

def xmlfile_download(request, pk):
    file = get_object_or_404(XMLFile, pk=pk)
    
    # Ensure the file is created/updated if not already present or outdated
    file_path = os.path.join(settings.MEDIA_ROOT, 'xml_files', f'{file.name}.xml')
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file.content)
        file.file.name = f'xml_files/{file.name}.xml'
        file.save()

    response = FileResponse(open(file.file.path, 'rb'), content_type='application/xml')
    response['Content-Disposition'] = f'attachment; filename={file.name}.xml'
    return response

def xmlfile_delete(request, pk):
    file = get_object_or_404(XMLFile, pk=pk)
    if request.method == 'POST':
        if file.file and os.path.exists(file.file.path):
            os.remove(file.file.path)  # Eliminar el archivo físico
        file.delete()  # Eliminar el registro de la base de datos
        return redirect('xmlfile_list')
    return render(request, 'xmlfile_confirm_delete.html', {'file': file})