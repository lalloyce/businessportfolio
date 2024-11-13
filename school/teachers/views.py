from django.shortcuts import render, redirect

from teachers.models import Teacher

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def insert(request):
    return render(request, 'insert.html')

def insert_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        avatar = request.FILES['avatar']

        teacher = Teacher(name=name, email=email, phone=phone, address=address, dob=dob, avatar=avatar)
        teacher.save()
        return redirect('/')

    return render(request, 'insert.html')

def view_data(request):
    teachers = Teacher.objects.all()
    return render(request, 'viewdata.html', {'teachers': teachers})