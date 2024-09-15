from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from KeyAcad_Data.models import All_course
from KeyAcad_Data.models import Certification
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages

# def home(request):
#     return HttpResponse("Home ")

def home(request):
    courses = All_course.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, "Welcome, Admin!")
                return redirect('/admin/')  # Redirect to the admin panel if admin
            else:
                messages.success(request, "Login successful!")
                return redirect('/admin/')  # Redirect regular users to the dashboard or homepage
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'my_app/index.html', {'courses':courses})

def viewcertificate(request):
    courses = All_course.objects.all()
    certificate = Certifications.objects.all()
    return render(request, 'my_app/viewcertificate.html',  {'courses':courses, 'certificate':certificate})
def about_us(request):
    courses = All_course.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, "Welcome, Admin!")
                return redirect('/admin/')  # Redirect to the admin panel if admin
            else:
                messages.success(request, "Login successful!")
                return redirect('/admin/')  # Redirect regular users to the dashboard or homepage
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'my_app/about.html', {'courses':courses})

def course_detail(request, slug):
    course = get_object_or_404(All_course, slug=slug)
    courses = All_course.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'my_app/register.html')

        # Check if the username or email is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'my_app/register.html', {'courses':courses})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'my_app/register.html', {'courses':courses})

        # Create and save the new user
        user = User(
            username=username, 
            first_name=firstname, 
            last_name=lastname, 
            email=email
        )
        user.password = make_password(password)  # Hash the password
        user.save()

        messages.success(request, "Registration successful!")
        return redirect('login')  # Redirect to a login page or wherever you like after registration
        user = authenticate(request, username=username, password=password)
    return render(request, 'my_app/Course.html', {'course': course, 'courses': courses})


def register(request):
    courses = All_course.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'my_app/register.html')

        # Check if the username or email is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'my_app/register.html', {'courses':courses})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'my_app/register.html', {'courses':courses})

        # Create and save the new user
        user = User(
            username=username, 
            first_name=firstname, 
            last_name=lastname, 
            email=email
        )
        user.password = make_password(password)  # Hash the password
        user.save()

        messages.success(request, "Registration successful!")
        return redirect('login')  # Redirect to a login page or wherever you like after registration
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, "Welcome, Admin!")
                return redirect('/admin/')  # Redirect to the admin panel if admin
            else:
                messages.success(request, "Login successful!")
                return redirect('/admin/')  # Redirect regular users to the dashboard or homepage
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'my_app/register.html',  {'courses':courses})
# Create your views here.
