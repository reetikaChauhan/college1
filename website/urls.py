from django.urls import path
from django.conf.urls import url
from website import views
urlpatterns = [
    path('<int:name>/',views.galleryphotos_view, name='nd'),
    url(r'hi/', views.galleryphotos_view, name='pp'),
    url(r'login/', views.loginadmin, name='ap'),
    url(r'adminn/', views.adminhome, name='as'),
    url(r'images_add/',views.add_image_view, name='nd'),

]