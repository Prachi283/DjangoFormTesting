from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	position=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	phone_no=models.IntegerField()

	def __str__(self):
		return self.name
