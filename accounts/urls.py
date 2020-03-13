from django.conf.urls import url
from django.contrib.auth import views as auth_views
## ^then dont need login logout views

from . import views

app_name = 'accounts'

urlpatterns = [
	url(r'login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
	
	#dont need to connect to my own views
	url(r'logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
	url(r'signup/$', views.SignUp.as_view(), name = 'signup'),
]

