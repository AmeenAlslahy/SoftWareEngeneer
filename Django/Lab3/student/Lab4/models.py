from django.db import models
import datetime
# # Create your models here.

class Guardian(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=9,unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=10)
    relation = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Students(models.Model):

    gend = [
        ('male','male'),
        ('female','female')
    ]
    levels = [
        ('مستوى اول',"مستوى اول"),
        ("مستوى ثاني","مستوى ثاني"),
        ("مستوى ثالث","مستوى ثالث"),
        ("مستوى رابع","مستوى رابع"),

    ]
    systems = [
        ("عام","عام"),
        ("موازي","موازي"),
        ("نفقة خاصة","نفقة خاصة"),
        ("مقاعد مجانية","مقاعد مجانية")
    ]
    states = [
        ('موقف قيد',"موقف قيد"),
        ("مستجد","مستجد"),
        ("باقي","باقي"),
    ]
    id = models.IntegerField(auto_created=True,primary_key=True)
    phone = models.CharField(null=True,blank=True,max_length=9,unique=True)
    email = models.EmailField(null=True,blank=True,unique=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    activ = models.CharField(default='نشط')
    state = models.CharField(default='مستجد',null=True,blank=True,choices=states)
    brithdate = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=6,null=True,blank=True,choices=gend)
    level = models.CharField(max_length=10,null=True,blank=True,choices=levels)
    system = models.CharField(default='عام',null=True,blank=True,max_length=20,choices=systems)
    guard = models.ForeignKey(Guardian,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


from django.db import models

class Students2(models.Model):
    GENDER_CHOICES = [
        ('ذكر', 'ذكر'),
        ('أنثى', 'أنثى'),
    ]
    
    STATUS_CHOICES = [
        ('نشط', 'نشط'),
        ('غير نشط', 'غير نشط'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    age = models.IntegerField(verbose_name="العمر")
    state = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="الحالة")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="الجنس")
    level = models.CharField(max_length=50, verbose_name="المستوى")
    email = models.EmailField(verbose_name="الإيميل")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    system = models.CharField(max_length=50, verbose_name="النظام")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"