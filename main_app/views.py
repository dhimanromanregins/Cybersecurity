from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm


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
	return render (request=request, template_name="register.html", context={"form":form})


def login_page(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})

def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):
	return render(request, 'index.html')