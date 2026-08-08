from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"Success.html")
    return render(request,'form.html',{'form':form})

def student_details(request,id):
    student = get_object_or_404(Student,id=id)
    return render(request,'student_details.html',{'student':student})

def edit_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    form = StudentForm(instance=student)
    return render(request,'form.html',{'form':form})

def delete_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request,'confirmation.html',{'student':student})