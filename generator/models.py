from django.db import models

class MapStatistics(models.Model):
    name = models.CharField(max_length=250)
    file = models.FileField(upload_to='map/', null=True, verbose_name="")
    
    class Meta:
        ordering = ['-id']
    
    
