from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models  import Profile
from django.contrib import messages

def upload(request):
    if request.method == 'POST':
        form  = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Picture Upload')
            return redirect('profile')
        else:
            messages.error(request,'Error Occured in Uploading File')
    else:
        form = ProfileForm()
    return render(request,'upload.html',{'forms':form})

def profile(request):
    profile = Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})