# from django import forms
# from .models import Students

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields = '__all__'


from django import forms
from .models import Students2

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students2
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'system': forms.TextInput(attrs={'class': 'form-control'}),
        }