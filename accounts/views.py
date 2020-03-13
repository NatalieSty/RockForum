from django.shortcuts import render
from django.urls import reverse_lazy

from . import forms
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
	#create new user
	form_class = forms.UserCreateForm

	#once signed, on success signup , to go login page
	#reverse lazy: dont execute until signing up
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'




