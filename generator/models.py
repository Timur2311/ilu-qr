from django.db import models

class MapStatistics(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nomi")
    file = models.FileField(upload_to='map/', null=True, verbose_name="Faylni yuklang")
    
    class Meta:
        ordering = ['-id']
    
    
