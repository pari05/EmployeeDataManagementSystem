# Create your views here.
from django.http import HttpResponse
from Employee.models import Employee
from django.template import Context, loader
from django.forms import ModelForm

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee

def FirstPage(request):
	all_employees = Employee.objects.all()
	#return HttpResponse("<H1>Parvesh here</H1><h3>brook was here</h3>")
	#return HttpResponse(all_employees)
	my_template = loader.get_template('Employee/FirstPage.html')
	my_context = Context({'all_employees':all_employees,})
	#return HttpResponse(my_template.render(my_context) + str(request.path))
	strV = ''
	if request.method == 'POST': # If the form has been submitted...		
		if 'Add' in request.POST:
			form = EmployeeForm()
			strV = "Add FOUND"
			my_template = loader.get_template('Employee/Add.html')
			my_context = Context({'form':form})
			return HttpResponse(my_template.render(my_context))
			
		if 'AddSubmit' in request.POST:
			strV = "ADD Submit"
			try:
				employee_selections_ids = request.POST.getlist('EmployeeID')
				for id in employee_selections_ids:
					emp = Employee.objects.get(EmployeeID=int(id))
					if emp:
						emp.delete()
			except:
				pass
			form = EmployeeForm(request.POST) # A form bound to the POST data
			if form.is_valid():
				form.save()
			else:
				return HttpResponse(str(form.errors))		
					
		if 'Delete' in request.POST:
			employee_selections_ids = request.POST.getlist('chk_employee_id')
			for id in employee_selections_ids:
				emp = Employee.objects.get(EmployeeID=int(id))
				emp.delete()
			#return HttpResponse(str(employee_selections_ids))
			strV = "Del FOUND"
			
		if 'Update' in request.POST:
			employee_selections_ids = request.POST.getlist('chk_employee_id')
			emp = ''
			for id in employee_selections_ids:
				emp = Employee.objects.get(EmployeeID=int(id))
			form = EmployeeForm(instance=emp)
			strV = "Add FOUND"
			my_template = loader.get_template('Employee/Add.html')
			my_context = Context({'form':form})
			return HttpResponse(my_template.render(my_context))
			strV = "Update FOUND"
		
	my_template = loader.get_template('Employee/FirstPage.html')
	my_context = Context({'all_employees':all_employees})
	return HttpResponse(my_template.render(my_context) + strV)
