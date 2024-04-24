from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import BookingForm, ContactForm
from .models import Departments, Doctors, Booking


# Create your views here.
def index(request):
    return render(request, 'index.html')


def authview(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def adminpage(request):
    return render(request, 'adminpage.html')


def booking(request):
    form = BookingForm()
    # print(form)
    if request.method == 'POST':
        data = BookingForm(request.POST)
        # print(data)
        if data.is_valid():
            data.save()
            return redirect('/')

    return render(request, 'booking.html', {'form': form})


def doctors(request):
    docs = Doctors.objects.all()
    print(docs)  # its like select * from doctors
    return render(request, 'doctors.html', {'docs': docs})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        data = ContactForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/')
    return render(request, 'contact.html', {'form': form})


# def department(request):
#     dict_dept = {
#         'dept': Departments.objects.all()
#     }
#     return render(request, 'department.html', dict_dept)

def department(request):
    dept = Departments.objects.all()
    return render(request, 'department.html', {'dept': dept})


def profile(request, my_id):
    print(my_id)
    prof = Doctors.objects.get(id=my_id)
    print(prof)
    return render(request, 'profile.html', {'prof': prof})
