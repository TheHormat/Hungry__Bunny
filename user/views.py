from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# from .decorators import unauthenticated_user

# Create your views here.

# @unauthenticated_user


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Account was created for {user}")
            return redirect('user:login')

    context = {'form': form}
    return render(request, "register.html", context)


# @unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.warning(request, 'Username or password incorrect')

        else:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("index")
