from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import EmployeForm
from .models import Employee
# Create your views here.
def HomePage(request):
    form = EmployeForm()  # 🔹 Initialize form outside of if block
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():  # 🔹 Always check if form is valid before saving
            form.save()
            form = EmployeForm()  # Reset form after saving
    
    datas = Employee.objects.all()

    context = {
        'form': form,
        'datas': datas
    }
    return render(request, 'app1/index.html', context)

def Update(request, id):
    user = get_object_or_404(Employee, id=id)  # 🔹 Use get_object_or_404 for safety

    if request.method == "POST":
        form = EmployeForm(request.POST, instance=user)  # 🔹 Correct form initialization
        if form.is_valid():
            form.save()
            return redirect('home')  # 🔹 Redirect to home after update
    
    else:
        user = Employee.objects.get(id=id)
        form = EmployeForm(instance=user)  # 🔹 Use correct form variable

    context = {
        'form': form  # 🔹 Use 'form' consistently (not 'forms')
    }
    return render(request, 'app1/update.html', context)

def Delete_record(request,id):
    user = Employee.objects.get(id=id)
    user.delete()
    return redirect('/')

def AboutUS(request):
    return render(request, 'app1/about.html')

def Services(request):
    return render(request, 'app1/services.html')
