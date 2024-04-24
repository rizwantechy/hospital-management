from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


from .models import Departments, Doctors, Booking, contact

admin.site.register(Departments)
admin.site.register(Doctors)


# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('id', 'c_name', 'c_phone', 'c_email', 'c_address', 'c_sub', '')


admin.site.register(contact)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')


admin.site.register(Booking, BookingAdmin)
