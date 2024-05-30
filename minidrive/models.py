from django.db import models

# Create your models here.
 
#Modelo para recibir archivos
class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)