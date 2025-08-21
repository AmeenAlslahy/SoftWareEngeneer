# from django.shortcuts import render
# from .models import Students
# from .forms import StudentForm
# # Create your views here.

# def students(request):
#     return render(request,'lab4/students.html',{'std':Students.objects.all()})

# def student(request):
#     return render(request,'lab4/student.html')



# def studentIn(request):

#     data = StudentForm(request.POST)
#     data.save()

#     return render(request,'lab4/base.html',{'x':StudentForm})

# def student_list(request):
#     query = request.GET.get('q', '')
    
#     if query:
#         students = Students.objects.filter(
#             Q(name__icontains=query) |
#             Q(email__icontains=query) |
#             Q(level__icontains=query) |
#             Q(phone__icontains=query)
#         )
#     else:
#         students = Students.objects.all()
    
#     return render(request, 'student_list.html', {'std': students})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Students2
from .forms import StudentForm
from django.core.paginator import Paginator
from django.shortcuts import render
# from .models import Students
from django.db.models import Count
import json
from datetime import datetime, timedelta

def student_list(request):
    # البحث
    search_query = request.GET.get('search', '')
    
    if search_query:
        students = Students2.objects.filter(
            name__icontains=search_query) | Students2.objects.filter(email__icontains=search_query) | Students2.objects.filter(phone__icontains=search_query)
    else:
        students = Students2.objects.all()
    
    # التقسيم إلى صفحات
    paginator = Paginator(students, 10)  # 10 طلاب لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lab4/list.html', {
        'students': page_obj,
        'search_query': search_query
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'lab4/add.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Students2, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'lab4/edit.html', {
        'form': form,
        'student': student
    })

def delete_student(request, student_id):
    student = get_object_or_404(Students2, id=student_id)
    
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    
    return render(request, 'lab4/confirm_delete.html', {'student': student})



def reports(request):
    # إحصائيات الطلاب حسب المستوى
    level_stats = Students2.objects.values('level').annotate(count=Count('id')).order_by('level')
    
    # إحصائيات الطلاب حسب الجنس
    gender_stats = Students2.objects.values('gender').annotate(count=Count('id'))
    
    # تحويل البيانات لصيغة JSON للرسوم البيانية
    level_labels = [item['level'] for item in level_stats]
    level_data = [item['count'] for item in level_stats]
    
    gender_labels = [item['gender'] for item in gender_stats]
    gender_data = [item['count'] for item in gender_stats]
    
    # تقرير الطلاب مع التصفية
    students = Students2.objects.all()
    
    # تصفية حسب المستوى إذا وجدت في الطلب
    level_filter = request.GET.get('level')
    if level_filter:
        students = students.filter(level=level_filter)
    
    context = {
        'students': students,
        'level_stats': json.dumps({
            'labels': level_labels,
            'data': level_data
        }),
        'gender_stats': json.dumps({
            'labels': gender_labels,
            'data': gender_data
        }),
        'total_students': Students2.objects.count(),
        'active_students': Students2.objects.filter(state='نشط').count(),
        'inactive_students': Students2.objects.filter(state='غير نشط').count(),
    }
    
    return render(request, 'lab4/reports.html', context)

def export_report(request):
    # هنا يمكنك إضافة كود لتصدير التقارير بصيغ مختلفة
    pass