from django.shortcuts import render
# Create your views here.
from django.contrib import messages 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from .models import Document
from django.http import HttpResponse
from django.conf import settings
import os

def uploadFile(request):
    if request.method == "POST":
        # Obteniendo los datos del formulario
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Guardar la información en la base de datos.
        document = Document(title=fileTitle, uploadedFile=uploadedFile)
        document.save()

    documents = Document.objects.all()

    return render(request, "minidrive/upload-file.html", context={"files": documents})

def eliminarArchivo(request):
    if request.method == 'POST':
        archivo_id = request.POST.get('archivo_id')
        archivo = get_object_or_404(Document, pk=archivo_id)
        
        # Eliminar el archivo físico
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(archivo.uploadedFile))
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
        
        # Eliminar el registro de la base de datos
        archivo.delete()

    return redirect('/drive')

def descargarArchivo(request, archivo_id):
    archivo = get_object_or_404(Document, pk=archivo_id)
    ruta_archivo = os.path.join(settings.MEDIA_ROOT, archivo.uploadedFile.name)
    with open(ruta_archivo, 'rb') as archivo_descargado:
        respuesta = HttpResponse(archivo_descargado.read())
        respuesta['Content-Type'] = 'application/force-download'
        respuesta['Content-Disposition'] = f'attachment; filename="{archivo.uploadedFile.name}"'
        return respuesta