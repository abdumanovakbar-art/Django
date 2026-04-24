from django.shortcuts import render, redirect

from apps.models import Student


# Create your views here.


def student_list_viwe(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request , 'student-list.html' , context=context)

def student_add_view(request):
    if request.method == 'GET':
        return render(request, 'student-add.html')
    elif request.method == 'POST':
        data = {
            "first_name": request.POST.get('first_name'),
            "last_name": request.POST.get('last_name'),
            "age": request.POST.get('age'),
            "gender": request.POST.get('gender'),
            "address": request.POST.get('address'),
            "course": request.POST.get('course'),
            "photo": request.FILES.get('photo'),
        }
        Student.objects.create(**data)
        return redirect('student-list')

def student_detail_view(request , id):
    student = Student.objects.filter(id=id).first()
    return render(request , 'student-detial.html' , context={'student':student} )


def student_delete_viwe(request , id):
    Student.objects.filter(id=id).delete()
    return redirect('student-list')


def student_edit_viwe(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.age = request.POST['age']
        student.gender = request.POST['gender']
        student.address = request.POST['address']
        student.course = request.POST['course']

        if request.FILES.get('photo'):
            student.photo = request.FILES['photo']

        student.save()
        return redirect('student-list')
    return render(request, 'student-edit.html', {'student': student})