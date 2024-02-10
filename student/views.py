from django.shortcuts import render, redirect
from student.models import Student
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
def mainPage(request):
    return render(request, 'main.html')



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username OR password is incorrect")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, "User was logged out!")
    return redirect('login')


def addStudent(request):
    if request.method=="POST":
        # Data fetching
        name  = request.POST.get("name")
        dob  = request.POST.get("dob")
        course  = request.POST.get("course")
        mobile  = request.POST.get("mobile")
        email  = request.POST.get("email")
        address  = request.POST.get("address")
        
        # create models object and set data
        student = Student()
        student.name = name
        student.dob = dob
        student.course = course
        student.mobile = mobile
        student.email = email
        student.address = address
        
        student.save()
        return redirect('home')
    return render(request, 'form.html')


def homePage(request):
    student = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        student = student.filter(name__icontains = search) | student.filter(course__icontains = search) | student.filter(mobile__icontains = search)

    data = {
        'students': student
    }     
    return render(request, 'home-page.html', data)


def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    print("Student deleted!")
    return redirect('home')



def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method=="POST":
        # Data fetching
        student.name  = request.POST.get("name")
        student.dob  = request.POST.get("dob")
        student.course  = request.POST.get("course")
        student.mobile  = request.POST.get("mobile")
        student.email  = request.POST.get("email")
        student.address  = request.POST.get("address")
        
        student.save()
        return redirect('home')
    data={
        'student':student
    }
    return render(request, 'form.html', data)

