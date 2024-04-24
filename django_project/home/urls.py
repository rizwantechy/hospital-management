from django.urls import path, include
from . import views, admin  # import views

urlpatterns = [
    path('', views.index, name='home'),         # these names are given to the hyperlinks to connect these pages
    path('about', views.about, name='about'),
    path('booking', views.booking, name='bookings'),
    path('doctors1', views.doctors, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='department'),
    path('profile/<int:my_id>/', views.profile, name='profile'),
    #path('adminpage', views.adminpage, name='adminpage'),# mapping to home url
]



#configure admin page

