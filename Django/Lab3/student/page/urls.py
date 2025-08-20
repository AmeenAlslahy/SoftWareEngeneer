from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('show/',views.show_student,name='show'),
    path('edit/',views.edit_student,name='edit'),
    path('delete/',views.delete_student,name='delete'),
    path('work/',views.home_work,name='work'),



]