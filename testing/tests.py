from django.test import TestCase
from .forms import Createform
from .models import Employee

class TestingFormTestCase(TestCase):
	def test_valid_form(self):
		name='prachi'
		email='pspatil708@gmail.com'
		position='software engineer'
		city='aurangabad'
		phone_no=8978675645
		obj=Employee.objects.create(name=name,email=email,position=position,city=city,phone_no=phone_no)
		data={'name':obj.name,'email':obj.email,'position':obj.position,'city':obj.city,'phone_no':obj.phone_no}
		form=Createform(data=data)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.cleaned_data.get('name'),obj.name)
		self.assertNotEqual(form.cleaned_data.get('email'),'another email')

	def test_invalid_form(self):
		name='prachi'
		email='pspatil708@gmail.com'
		position='software engineer'
		city='aurangabad'
		phone_no=8978675645
		obj=Employee.objects.create(name=name,email=email,position=position,city=city,phone_no="")
		data={'name':obj.name,'email':obj.email,'position':obj.position,'city':obj.city,'phone_no':obj.phone_no}
		form=Createform(data=data)
		self.assertTrue(form.is_valid())
		self.assertTrue(form.errors)

	def test_form_validation_for_blank_items(self):
		form = Createform(data={'name':''})
		form.save()

	def test_form_validation_for_blank_items(self):
		form=Createform(data={'email':''})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['email'],["You can't have an empty list item"])


	def test_home_page_renders_home_template(self):
		response = self.client.get('/home')
		self.assertTemplateUsed(response, 'home.html') 

	def test_home_page_uses_item_form(self):
		response = self.client.get('/home')
		self.assertIsInstance(response.context['form'], Createform) 