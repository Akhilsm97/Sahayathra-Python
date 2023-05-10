from django.db import models

# Create your models here.

class giver_reg(models.Model):
    profile_pic = models.ImageField(upload_to='pic_upload/images')
    giver_name = models.CharField(max_length=20)
    aaddhar = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mob_no = models.CharField(max_length=20)
    native = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    veh_type = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class taker_reg(models.Model):
    profile_pic = models.ImageField(upload_to='pic_upload/images')
    taker_name = models.CharField(max_length=20)
    aaddhar = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mob_no = models.CharField(max_length=20)
    native = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class login_table(models.Model):
    username = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class make_trips(models.Model):
    giver_name = models.CharField(max_length=20)
    start = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    veh_model = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    bal_seat = models.CharField(max_length=20)
    trip_id = models.CharField(max_length=20)


class requested_trip(models.Model):
    taker_name = models.CharField(max_length=20)
    giver_name = models.CharField(max_length=20)
    start = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    veh_model = models.CharField(max_length=20)
    trip_status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=20)
    trip_id = models.CharField(max_length=20)
    pay_date = models.CharField(max_length=20)



