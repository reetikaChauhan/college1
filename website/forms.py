from django import forms
from .models import *

class admin_form(forms.ModelForm):
    class Meta:
        model = admin_model
        fields = ['username', 'password']

class events_Form(forms.ModelForm):
    class Meta:
        model = events_model
        fields = ['event_name', 'event_desc']

eventName = []

class images_Form(forms.Form):
    p = events_model.objects.all().values('event_name').distinct()
    for x in p:
        eventName.append((x['event_name'], x['event_name']))
    name = forms.CharField(label="Name",widget=forms.Select(choices=eventName))
    Images = forms.FileField(label="Images", max_length=225)

eventName1 = []
class newspaper_Form(forms.Form):
    pp = events_model.objects.all().values('event_name').distinct()
    for x in pp:
        eventName1.append((x['event_name'], x['event_name']))
    name = forms.CharField(label="Name", widget=forms.Select(choices=eventName))
    newspaperPictures = forms.FileField(label="Images", max_length=225)

class student_placed_form(forms.Form):
    choices11 = [('btech (cse)', 'BTECH (CSE)'), ('btech (me)', 'BTECH (ME)'), ('btech (ece)', 'BTECH (ECE)'), ('btech (civil)', 'BTECH (CIVIL)')]
    student_name = forms.CharField(label="Name",max_length=225)
    roll_no = forms.CharField(label="Roll_no",max_length=225)
    stream =  forms.CharField(label="Stream",widget=forms.Select(choices=choices11))
    company_name = forms.CharField(label="Company",max_length=225)
    picture = forms.FileField(label="Picture", max_length=225)


class newsletter_Form(forms.ModelForm):
    class Meta:
        model = newsletterss_lkce
        fields =['name','title','newsletters']


class add_streamForm(forms.ModelForm):
    class Meta:
        model = stream_add_model
        fields = ['name','icon']

class academic_form(forms.ModelForm):
    class Meta:
        model = academic_calender
        fields = ['calender']
		
class information_form(forms.Form):
    choicesinfo = [('news', 'NEWS'), ('placements', 'PLACEMENTS'), ('upcoming events', 'UPCOMING EVENTS'), ('alumni', 'ALUMNI')]
    type_info = forms.CharField(label="Type", widget=forms.Select(choices=choicesinfo))
    heading = forms.CharField(widget=forms.Textarea())
    info = forms.CharField(widget=forms.Textarea())

class hpage_img(forms.ModelForm):
    class Meta:
        model = homepage_img
        fields = ['home_image']

class placedupdateForm(forms.ModelForm):
    class Meta:
        model = student_placed
        fields = "__all__"








