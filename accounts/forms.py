from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm	

class UserCreateForm(UserCreationForm):
	## call usercreationform when user want to sign up
	## set up meta class
	## these are the fields user to be about to access
	class Meta:
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()

	def __init__(self, *args, **kwargs):
		## setting up label for form fields
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Display Name'
		self.fields['email'].label = "Emaill Address"




		