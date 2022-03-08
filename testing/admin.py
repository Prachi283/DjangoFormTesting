from django.contrib import admin
from .models import Employee

# Register ModelAdmin Class 
class EmployeeAdmin(admin.ModelAdmin):
	list_display=('name','email','position','city','phone_no',)




# Register your models here.

admin.site.register(Employee,EmployeeAdmin)