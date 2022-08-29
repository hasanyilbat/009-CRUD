from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
##!importları unutma

# Create your views here.
def index(request):
    return render(request, 'fscohort/index.html')  ##! direkt template içine baktığından template içindeki klasör adı ve html dosyasını yazmam yeterli.


#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#! /*/                                     /*/
#! /*/         CRUD  - READ(GET)           /*/
#! /*/                                     /*/
#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/



def student_list(request):
    students  = Student.objects.all() ##! ile bütün verilere eriştik
    context = {                        ##! context yapısına aldık html dosyası içinde kullanıcaz.
        'students': students,
    }
    return render(request, 'fscohort/student_list.html', context)        ##!render edilmesini sağladık bununla birlikte contexti yolladık.


#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#! /*/                                     /*/
#! /*/         CRUD  - CREATE (POST)       /*/
#! /*/                                     /*/
#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form":form
    }
    return render(request, 'fscohort/student_add.html', context)



#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#! /*/                                     /*/
#! /*/         CRUD  - UPDATE (POST)       /*/
#! /*/                                     /*/
#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

def student_update(request, id):
    student =Student.objects.get(id=id) #! update edilcek nesneyi belirttik.
    form = StudentForm(instance=student) #!parametre olarak az önce aldığımız studentı ekledik.
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'fscohort/student_update.html', context)

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect(list)
    context = {
        'student':student
        }
    
    return render(request, 'fscohort/student_delete.html', context )





#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#! /*/                                     /*/
#! /*/         STUDENT DETAIL PAGE         /*/
#! /*/                                     /*/
#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

def student_detail(request, id):        
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)