from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin


def SignupPage(request):   
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            messages.error(request, "Account creation failed")

        return redirect("index")

    form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is None:
            return HttpResponse("Username or Password is incorrect!!!")

        login(request, user)
        return redirect('index')
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('user:login')


class DeleteUser(SuccessMessageMixin,generic.DeleteView):
    model = User
    template_name = 'delete_user_confirm.html'
    success_url  = reverse_lazy('index')