from django.db import models
import os
from django.conf import settings


class XMLFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='xml_files/', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'xml_files')):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'xml_files'))
        # Save the XML content to a file
        if not self.file:
            file_path = os.path.join(settings.MEDIA_ROOT, 'xml_files', f'{self.name}.xml')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.content)
            self.file.name = f'xml_files/{self.name}.xml'
        super().save(*args, **kwargs)