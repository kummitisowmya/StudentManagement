from django import forms
from django.contrib.auth.models import User
from students.models import *


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['contact_info', 'address', 'fees_paid']  # Added fees_paid field
        widgets = {
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fees_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class StudentCourseForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = StudentCourse
        fields = ['student', 'course']