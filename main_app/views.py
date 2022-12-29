from django.shortcuts import render, redirect
from .forms import CustomUserForm , ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def demo(request):

    return render(request, 'demo.html')

# def register_page(request):
#     if request.user.is_anonymous:
#         form = CustomUserForm(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             form.save()
#             new_user = authenticate(username=username, password=password)
#             if new_user is not None:
#                 login(request, new_user)
#                 return redirect('demo')
#
#     else:
#         return redirect('demo')
#     form = CustomUserForm()
#     context = {'form': form}
#     return render(request, 'register.html', context)
@csrf_exempt
def register_page(request):
	if request.method == "POST":
		form = CustomUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomUserForm()
	return render (request=request, template_name="authentication/register.html", context={"form":form})


def login_page(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				request.session['user_id'] = user.id
				request.session['user_email'] = user.email
				print(user.id, user.email)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="authentication/login.html", context={"form":form})

def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):
	return render(request, 'index.html')

@csrf_exempt
def contactus(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
			email_message = form.cleaned_data['message']
			send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
			messages.success(request, "Message sent")
			return redirect('contact')
		messages.error(request, "Please filll the form properly")
	form = ContactForm()
	return  render(request, 'contact.html', context={'form':form})
