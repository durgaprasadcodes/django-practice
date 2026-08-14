from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .form import StudentForm

def home(request):
    studnets = Student.objects.all()
    return render(request,'home.html',{'students':studnets})

def add_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
    return render(request,'student_form.html',{'form':StudentForm()})

def edit_students(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
    return render(request,'student_form.html',{'form':StudentForm(instance=student)})
def student_list(request):
    studnets = Student.objects.all()
    return render(request,'student_functions.html',{'students':studnets})
def delete(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request,'student_functions.html',{'student':student}) 