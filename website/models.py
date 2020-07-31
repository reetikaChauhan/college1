from django.db import models

# Create your models here.
class admin_model(models.Model):
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

class events_model(models.Model):
    event_name = models.CharField(max_length=225)
    event_desc = models.TextField()

class Img_lkcee(models.Model):
    name = models.CharField(max_length=50)
    Images = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class newspaper_lkcee(models.Model):
    newspaperPictures = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class newsletterss_lkce(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    newsletters = models.FileField(upload_to='images/')

class stream_add_model(models.Model):
    name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    icon = models.FileField(upload_to='images/')


class student_placed(models.Model):
    picture = models.ImageField(upload_to='images/')
    student_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    stream =  models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class feedback_model(models.Model):
    name =  models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=250)
    phone = models.CharField(max_length=500)
    message = models.TextField(max_length=700)

class academic_calender(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    calender = models.ImageField(upload_to='images/')

class information_model1(models.Model):
    type_info = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    info =  models.TextField()
    heading = models.TextField()

class homepage_img(models.Model):
    home_image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


