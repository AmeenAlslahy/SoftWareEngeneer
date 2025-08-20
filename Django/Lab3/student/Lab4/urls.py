from django.urls import path
from . import views

# urlpatterns =[
#     path('',views.students,name='students'),
#     path('student/',views.student,name='student'),   
#     path('studentIn/',views.studentIn,name='studentIn'),

# ]

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('reports/', views.reports, name='reports'),
    path('export-report/', views.export_report, name='export_report'),
]