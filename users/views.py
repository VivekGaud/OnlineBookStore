from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from users.models import users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def register(request):
	if request.method =="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request,f"you are logged in: { username }")
			request.session['username']=username
			return redirect("homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = UserCreationForm
	context ={
	"form":form
	}
	return render(request, 'users/register.html',context)

def user_login(request):
	if request.method =="POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request,f"you are logged in as: { username }")
				request.session['username']=username
				cont={
				"username":username
				}
				return redirect("homepage")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	print(request.session)
	form = AuthenticationForm()
	context ={
	"form":form
	}
	return render(request, 'users/login.html',context)



def user_logout(request):
	logout(request)
	messages.info(request,"logged out")
	return redirect("homepage")