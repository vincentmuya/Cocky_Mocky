from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name ='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^services/', views.services, name='services'),
    ]
