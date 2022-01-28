from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from .forms import SignupForm

# Create your views here.
def login(request):
	return render(request, 'login.html', {})

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')
	
class UserRegistrationView(generic.CreateView):
	form_class = SignupForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.CreateView):
	form_class = UserChangeForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user
