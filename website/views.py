from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound, HttpRequest
import datetime
from django.template import loader
from django.contrib import messages
from django.template import RequestContext
#from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
#from models  import *
from website.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def adminhome(request):
    m ='false'
    if request.session.has_key('boll'):
        m = request.session['boll']
        print("flag", m)
    if(m == 'true'):
        return render(request, "website/adminn.html")
    else:
        message = "please login first"
        print("login first")
        return render(request, 'website/login__admin.html', {'message': message})

def index_view(request):
    news_card1 = information_model1.objects.filter(type_info='news')
    print('nc', news_card1)
    return render(request,"website/index.html",{'nc': news_card1 })

@csrf_exempt
def loginadmin(request):
    # if post request came
    flg1 = 'false'
    nn = 'h'
    if request.session.has_key('flg1'):
        flg1 = request.session['flg1']
        print("flag", flg1)
    if (flg1 != 'true'):
        if request.method == 'POST':
            # getting values from post
            userid = request.POST.get('userid')
            password = request.POST.get('password')
            request.session['flg1'] = 'true'
            print("flg1",flg1)
            # adding the values in a context variable
            '''context = {
                'userid': userid,
                'password': password

            }'''

            if admin_model.objects.filter(userid=userid, password=password).exists():

                return HttpResponseRedirect("/adminn")


            else:
                message = 'Incorrect Password'
                return render(request, "website/login.html", {'message': message,'flg1': flg1})

        else:
            return render(request, "website/login.html",{'flg1': flg1})

def admin_login(request):
    flg1 = 'false'
    nn = 'h'
    if request.session.has_key('boll'):
        flg1 = request.session['boll']
        print("flag", flg1)
    if (flg1 != 'true'):
        if request.method == "POST":
            data = request.POST  # getting data from the form
            form = admin_form(data)
            if form.is_valid():
                u_username = form.cleaned_data["username"]
                u_password = form.cleaned_data["password"]
                p = admin_model.objects.filter(username= u_username, password=u_password)
                print("00000", p)
                # sessions
                if (p.count() > 0):
                    print("valid user")
                    # print(name)
                    request.session['boll'] = 'true'
                    return HttpResponseRedirect("/adminn")
                else:
                    print("try again")
                    return HttpResponseNotFound('<h1> no page here </h1>')
            else:
                print("else block")
                return render(request, "website/login__admin.html", {"form": form, 'boll': flg1})
        else:
            form = admin_form()
            print("third else block")
            return render(request, "website/login__admin.html", {"form": form, 'boll': flg1})
    else:
        return render(request, "website/adminn.html", {'boll': flg1, 'message': 'you are already logged in'})


def admin_logout(request):
    for key in list(request.session.keys()):
        print("key",key)
        del request.session[key]
    return HttpResponseRedirect("/login__admin")

def events_view(request):
        if request.method == 'POST':
            form = events_Form(request.POST, request.FILES)
            if form.is_valid():
                u_event_name = form.cleaned_data["event_name"]
                u_event_desc = form.cleaned_data["event_desc"]
                p = events_model(event_name=u_event_name, event_desc=u_event_desc)
                p.save()
                return redirect('success')
        else:
            form = events_Form()
        return render(request, 'website/events_add.html', {'form': form})



def add_image_view(request):
    if request.method == 'POST':
        form = images_Form(request.POST, request.FILES)

        if form.is_valid():
            u_name = form.cleaned_data["name"]
            u_images = form.cleaned_data["Images"]
            i = Img_lkcee(name=u_name, Images=u_images)
            i.save()
            return redirect('success')
    else:
        form = images_Form()
    return render(request, 'website/images_add.html', {'form': form})





def success(request):
    return HttpResponse('<h1> Successfully Uploaded !</h1>')

def gallery_display(request):
    q = Img_lkcee.objects.values('name').distinct()
    q = list(q)
    k = []
    for i in q:
        k.append(i['name'])
    print(k)
    t =[]
    for j in k:
        m = Img_lkcee.objects.filter(name=j)
        print(m[0].Images)
        t.append(m[0])
    print(t)
    return render(request, "website/photogallery.html",{'q': q,'t':t})

def galleryphotos_view(request):
    if request.method == 'GET':
        sku = request.GET.get('name')
        if not sku:
            return render(request, 'website/photogallery.html')
        else:
            # now you have the value of sku
            # so you can continue with the rest
            print('name',sku)
            l = Img_lkcee.objects.filter(name=sku)
            t = events_model.objects.filter(event_name = sku)
            return render(request, 'website/galleryphotos.html',{'l':l,'t':t,'sku':sku})

def newspaper_view(request):
    if request.method == 'POST':
        form = newspaper_Form(request.POST, request.FILES)

        if form.is_valid():
            u_name = form.cleaned_data["name"]
            u_newspaperPictures = form.cleaned_data["newspaperPictures"]
            n = newspaper_lkcee(name=u_name, newspaperPictures=u_newspaperPictures)
            n.save()
            return redirect('success')
    else:
        form = newspaper_Form()
    return render(request, 'website/newspaperpics_add.html', {'form': form})

def rouview(request):
    qq1 = stream_add_model.objects.all()
    return render(request, 'website/rou.html',{'qq1':qq1})



def newspaperalbum_view(request):
    qq = newspaper_lkcee.objects.values('name').distinct()
    qq = list(qq)
    kk = []
    for i in qq:
        kk.append(i['name'])
    print('list of names',kk)
    tt = []
    for j in kk:
        m = newspaper_lkcee.objects.filter(name=j)
        print('j',j)
        print(m[0]. newspaperPictures)
        tt.append(m[0])
    print('name',tt)
    return render(request, 'website/newspapersalbum.html', {'ob': tt})

def newspaperdisplay_view(request):
    if request.method == 'GET':
        sku1 = request.GET.get('name')
        if not sku1:
            return render(request, 'website/newspapersalbum.html')
        else:
            # now you have the value of sku
            # so you can continue with the rest
            print('sk1', sku1)
            l = newspaper_lkcee.objects.filter(name=sku1)
            return render(request, 'website/newspaper_display.html', {'l': l,'sku':sku1})

def newsletteradd_view(request):
    if request.method == 'POST':
        form = newsletter_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = newsletter_Form()
    return render(request, 'website/newsletter_add.html', {'form': form})

def newsletterdisplay_view(request):
    j = newsletterss_lkce.objects.all()
    return render(request,'website/newletter_display.html',{'obj':j})

def placed_studentview(request):
    if request.method == 'POST':
        form = student_placed_form(request.POST, request.FILES)

        if form.is_valid():
            u_student_name =  form.cleaned_data["student_name"]
            u_roll_no = form.cleaned_data["roll_no"]
            u_stream = form.cleaned_data["stream"]
            u_company_name = form.cleaned_data["company_name"]
            u_picture = form.cleaned_data["picture"]
            ps = student_placed(student_name = u_student_name,roll_no = u_roll_no,stream = u_stream, company_name = u_company_name,picture=u_picture)
            ps.save()
            return redirect('success')
    else:
        form = student_placed_form()
    return render(request, 'website/placed_student.html', {'form': form})

def placed_student_list_view(request):
    psl = student_placed.objects.all()
    return render(request,'website/placedList.html',{'psl':psl})


@csrf_exempt
def edit1(request, pk):
    students = student_placed.objects.get(pk=pk)
    return render(request, "system1/updateTeach.html", {'l1': students})

    # template = loader.get_template('system/update.html',)

@csrf_exempt
def placed_update_view(request,pk):

    psu = student_placed.objects.get(pk=pk)
    form = placedupdateForm(request.POST, instance=psu)
    if form.is_valid():
        form.save()
        students = student_placed.objects.all()
        template = loader.get_template('website/teachinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)

    return render(request, 'system1/updateTeach.html', {'Useradd': Useradd})



def student_placed_album(request):
    qq1 = stream_add_model.objects.all()
    return render(request,'website/placed_studentalbum.html',{'qq1':qq1})

def stream_add_view(request):
    if request.method == 'POST':
        form = add_streamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = add_streamForm()
    return render(request, 'website/add_streams.html', {'form': form})

def student_placed_displayview(request):
    if request.method == 'GET':
        sku = request.GET.get('name')
        if not sku:
            return render(request, 'website/placed_studentalbum.html')
        else:
            # now you have the value of sku
            # so you can continue with the rest
            print('name',sku)
            l = student_placed.objects.filter(stream=sku)
            return render(request, 'website/student_placed_display.html',{'l':l,'sku':sku})
			
def infoview(request):
    if request.method == 'POST':
        form = information_form(request.POST,request.FILES)
        if form.is_valid():
            u_type_info = form.cleaned_data["type_info"]
            u_info = form.cleaned_data["info"]
            u_heading = form.cleaned_data["heading"]
            pi = information_model1(type_info=u_type_info, info=u_info,heading= u_heading)
            pi.save()
            return redirect('success')
    else:
        form = information_form()
    return render(request, 'website/informationpage.html', {'form': form})			
			
def newscard_news(request):
    news_card = information_model1.objects.filter(type_info = 'news')
    news_card1 = list(news_card)
    print(news_card[0].heading)
    return render(request,'website/newscardsdisplay.html',{'nc': news_card})

def complete_newsView(request):
    l1 = information_model1.objects.filter(type_info='news')
    l2 = information_model1.objects.filter(type_info='placements')
    l3 = information_model1.objects.filter(type_info='upcoming events')
    l4 = information_model1.objects.filter(type_info='alumni')
    return render(request, 'website/complete_news.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4})


def aboutview(request):
    return render(request,"website/about.html")

def home(request):
    news_card1 = information_model1.objects.filter(type_info='news')
    print('nc', news_card1)
    nc2 = information_model1.objects.filter(type_info='placements')
    nc3 = information_model1.objects.filter(type_info='upcoming events')
    nc4 = information_model1.objects.filter(type_info='alumni')
    ig = homepage_img.objects.all()
    return render(request,'website/index.html',{'nc':news_card1,'nc2':nc2,'nc3':nc3,'nc4':nc4,'ig':ig})

def baseview(request):
    return render(request,'website/base.html')
	
	
def Ourgoverningbody(request):
    return render(request,"website/Ourgoverningbody.html")
def Ourcoreteam(request):
    return render(request,"website/Ourcoreteam.html")
def infrast(request):
    return render(request,"website/infrast.html")
def p1(request):
    return render(request,"website/p1.html")
def p2(request):
    return render(request,"website/p2.html")
def p3(request):
    return render(request,"website/p3.html")
def p4(request):
    return render(request,"website/p4.html")
def j(request):
    return render(request,"website/j.html")
def btech(request):
    return render(request,"website/btech.html")
def diploma(request):
    return render(request,"website/diploma.html")
def bvoc(request):
    return render(request,"website/bvoc.html")
def bsc(request):
    return render(request,"website/bsc.html")
def fee(request):
    return render(request,"website/fee.html")
def place1(request):
    return render(request,"website/place1.html")
def place2(request):
    return render(request,"website/place2.html")
def place3(request):
    return render(request,"website/place3.html")
def scriptview(request):
    return render(request,"website/scripty.html")
@csrf_exempt
def contact_view(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        name = request.POST.get('na')
        subject = request.POST.get('subject')
        phone =  request.POST.get('phone')
        message = request.POST.get('message')
        request.session['myuser'] = name

        email = request.POST.get('mail')

        # adding the values in a context variable
        context = {
            'name': name,
            'subject': subject,
            'phone': phone,
            'email': email,
            'message': message
         }
        fb = feedback_model()
        fb.name = name
        fb.phone = phone
        fb.email = email
        fb.subject = subject
        fb.message = message
        fb.save()
        message = 'success'
        return render(request,'website/contactus.html',{'message':message})
    else:
        template = loader.get_template('website/contactus.html')
        return HttpResponse(template.render())

def academic_view(request):
    if request.method == 'POST':
        form = academic_form(request.POST, request.FILES)

        if form.is_valid():
            u_images = form.cleaned_data["calender"]
            ia =  academic_calender( calender = u_images )
            ia.save()
            message ='success'
            return render(request, 'website/adminn.html', {'message': message})
    else:
        form = academic_form()
    return render(request, 'website/academic.html', {'form': form})

def calender_display(request):
    jc = academic_calender.objects.all()
    return render(request,'website/calender_show.html',{'j':jc})

def hpage_view(request):
    if request.method == 'POST':
        form = hpage_img(request.POST, request.FILES)

        if form.is_valid():
            u_home_image = form.cleaned_data["home_image"]
            iah = homepage_img(home_image=u_home_image)
            iah.save()
            message = 'success'
            return render(request, 'website/adminn.html', {'message': message})
    else:
        form = hpage_img()
    return render(request, 'website/hpage.html', {'form': form})




