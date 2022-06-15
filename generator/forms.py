from django.forms import ModelForm
from .models import MapStatistics

class UploadFileForm(ModelForm):
    class Meta:
        model = MapStatistics
        fields = ['name', 'file']
        