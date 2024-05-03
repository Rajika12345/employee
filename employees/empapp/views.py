from django.shortcuts import render,redirect
from empapp.models import Employee
from django.views.generic import View
from empapp.forms import EmployeeForm

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"employee_list.html",{"data":qs})

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeForm()
        return render(request,'employee_add.html',{"form":form})

    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST,files=request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            Employee.objects.create(**data)
            return redirect('employee-list')
        return render(request,'employee_add.html',{"form":form})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs) #kwargs={"pk":6}
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,'employee_detail.html',{'data':qs})

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        return redirect('employee-list')

class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employee.objects.get(id=id)
        form=EmployeeForm(instance=employee_object)
        return render(request,'employee_edit.html',{'form':form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employee.objects.get(id=id)
        form=EmployeeForm(request.POST,instance=employee_object,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        else:
            return render(request,'employee_edit.html',{'form':form})