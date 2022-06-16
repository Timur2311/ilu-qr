from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions
from .forms import UploadFileForm
from .models import MapStatistics

def index(request):   
    name = ""
    last_file = ""
    file_url = ""
    if request.method == 'POST':        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data 
            name = cd['name']      
            form.save()
            last_file = MapStatistics.objects.all()[0]
            file_url = request.build_absolute_uri(last_file.file.url) 
            file_url = str(file_url)          
    else:
        form = UploadFileForm()
    context = dict(
        my_options=QRCodeOptions(size="T",image_format="png", error_correction='L'),
        form = form,
        last_file = file_url,
        name = name,
    )
    return render(request, 'index.html', context = context)
