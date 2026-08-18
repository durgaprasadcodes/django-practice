from django.shortcuts import render
from django.contrib import messages

def index(request):
    messages.debug(request,'This is debug Message')
    messages.info(request,'This is a Info Meassgae')
    messages.success(request,'This is a Success Message')
    messages.warning(request,'This is a Warning Message')
    return render(request,'index.html')