from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "minidrive"

urlpatterns = [
    path("", views.uploadFile, name="uploadFile"),
    path("descargar/<int:archivo_id>", views.descargarArchivo, name="descargar"),
    path("eliminar", views.eliminarArchivo, name="eliminar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)