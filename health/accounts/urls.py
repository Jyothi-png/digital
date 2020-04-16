from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('docregister', views.docregister, name="docregister"),
    #path('home', views.home, name="home"),
    path('userregister', views.userregister, name="userregister"),
    path('pharmregister', views.pharmregister, name="pharmregister"),
    path('pdetail', views.PDetails, name="pdetail"),
    path('changedetails', views.changedetails, name='changedetails')
]
