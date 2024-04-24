from django.db import models


class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
    doc_about = models.CharField(max_length=500, null='true', blank='true')
    doc_phone = models.IntegerField(null='true', blank='true')

    def __str__(self):
        return 'Dr ' + self.doc_name + ' - (' + self.doc_spec + ')'


class Booking(models.Model):
    p_name = models.CharField(max_length=200)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name


class contact(models.Model):
    c_name = models.CharField(max_length=200)
    c_email = models.EmailField()
    c_phone = models.IntegerField()
    c_address = models.CharField(max_length=300, null='true', blank='true')
    c_sub = models.CharField(max_length=500)

    def __str__(self):
        return self.c_name +'  - '+  self.c_sub
