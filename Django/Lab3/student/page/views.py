from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request,'page/index.html')


def home(request):
    std = {'name':'ameen abdu mohammad najy alsalahy',
           'age':23,'address':'IBB'}
    return render(request,'page/home.html',std)

def show_student(requset):
     std = {'name':'ameen abdu mohammad najy alsalahy',
       'age':23,'address':'IBB'}
     return render(requset,'page/showstudent.html',std)

def edit_student(requset):
    return render(requset,'page/editstudent.html')

def delete_student(requset):
    return render(requset,'page/deletestudent.html')



def home_work(requset):
    context = {
        'user': requset.user,
        'today': timezone.now(),
        'products': [
            {'name': 'حاسوب محمول', 'price': 2500, 'stock': 15},
            {'name': 'هاتف ذكي', 'price': 1800, 'stock': 8},
            {'name': 'سماعات', 'price': 300, 'stock': 0},
        ],
        'total_price': 2500 + 1800 + 300,
        'search_query': 'ذكي',
       }
    return render(requset, 'page/homework.html', context)