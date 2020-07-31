"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
#from django.views.static import serve
from website import views
from django.conf.urls.static import static
from college import settings
from website.views import *
import website.views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^adminn/', views.adminhome, name='as'),
    url(r'^login__admin/', views.admin_login, name='as'),
    url(r'^logout/',views.admin_logout,name='la'),
	url(r'^index/', views.home, name='home'),
    url(r'^login/', views.loginadmin, name='ap'),
    url(r'^images_add/', views.add_image_view, name='showAssign'),
    path('images_add/', add_image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
    url(r'^photogallery/',views.gallery_display, name='pg'),
    url(r'^galleryphotos/',views.galleryphotos_view, name= 'nd'),
    url(r'^newspaperpics_add/',views.newspaper_view, name= 'newspaper_view'),
    url(r'^newspapersalbum/',views.newspaperalbum_view, name= 'newspaperalbum_view'),
    url(r'^newspaper_display/',views.newspaperdisplay_view, name= 'newspaperdisplay_view'),
    url(r'^newsletter_add/',views.newsletteradd_view, name= 'newsletteradd_view'),
    url(r'^newletter_display/', views.newsletterdisplay_view, name='newsletterdisplay_view'),
    url(r'^events_add/',views.events_view, name='pg'),
    url(r'^placed_student/',views.placed_studentview, name='psv'),
    url(r'^placed_studentalbum/',views.student_placed_album, name='psvv'),
    url(r'^add_streams/',views.stream_add_view,name = 'asss'),
    url(r'^student_placed_display/',views.student_placed_displayview,name='spd'),
	url(r'^newscardsdisplay/',views.newscard_news,name = 'ncd'),
    url(r'^complete_news/',views.complete_newsView,name = 'cn'),
	url(r'^about/', views.aboutview, name='about'),
	url(r'^Ourgoverningbody/', views.Ourgoverningbody, name='Ourgoverningbody'),
    url(r'^Ourcoreteam/', views.Ourcoreteam, name='Ourcoreteam'),
    url(r'^infrast/$', views.infrast, name='infrast'),
    url(r'^p1/', views.p1, name='p1'),
    url(r'^p2/', views.p2, name='p2'),
    url(r'^p3/', views.p3, name='p3'),
    url(r'^p4/', views.p4, name='p4'),
    url(r'^j/', views.j, name='j'),
    url(r'^btech/', views.btech, name='btech'),
    url(r'^diploma/', views.diploma, name='diploma'),
    url(r'^bvoc/', views.bvoc, name='bvoc'),
    url(r'^bsc/', views.bsc, name='bsc'),
    url(r'^fee/', views.fee, name='fee'),
    url(r'^place1/', views.place1, name='place1'),
    url(r'^place2/', views.place2, name='place2'),
    url(r'^place3/', views.place3, name='place3'),
    url(r'^contactus/', views.contact_view, name='contact'),
    url(r'^academic/', views.academic_view, name='av'),
    url(r'^calender_show/', views.calender_display, name='av'),
    url(r'^informationpage/',views.infoview,name='ip'),
    url(r'^complete_news/', views.complete_newsView, name='ip'),
    url(r'^hpage/', views.hpage_view, name='ip'),
    url(r'^rou/',views.rouview,name='ro'),
    url(r'^scripty/',views.scriptview,name='scripty'),
    url(r'^placedList/',views.placed_student_list_view,name='pl'),
    url(r'^placed_update/',views.placed_update_view,name='pl'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)