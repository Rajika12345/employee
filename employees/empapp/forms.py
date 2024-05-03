from django import forms
from empapp.models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields="__all__"
        widgets={
            "employee_name":forms.TextInput(attrs={'class':'form-control'}),
            "joining_date":forms.DateInput(attrs={'class':'form-control',"type":"date"}),
            "gender":forms.TextInput(attrs={'class':'form-control'}),
            "dob":forms.DateInput(attrs={'class':'form-control',"type":"date"}),
            "email":forms.TextInput(attrs={'class':'form-control'}),
            "phone":forms.TextInput(attrs={'class':'form-control'}),
            "employee_image":forms.FileInput(attrs={'class':'form-control'}),
            "address":forms.Textarea(attrs={'class':'form-control','rows':5}),
            "salary":forms.TextInput(attrs={'class':'form-control'}),
            "about":forms.Textarea(attrs={'class':'form-control','rows':5}),
            "designation":forms.TextInput(attrs={'class':'form-control'}),
        }