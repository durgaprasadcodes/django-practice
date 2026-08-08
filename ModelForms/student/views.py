from django.shortcuts import render
from .form import StudentForm

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render(request,'student_form.html',{'form':StudentForm()})
