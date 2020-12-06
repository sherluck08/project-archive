from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(
                request, "You have successfully register, you can login below")
            return redirect("login")
        else:
            print(form.errors)
            print("form not valid")
            form = RegistrationForm()
            return render(request, 'account/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})


def signin(request):
    logout(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if username.lower() == "group4com226" and password == "1234567":
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    # messages.success(
                    #     request, "You have successfully logged in")
                    return redirect("admin-home")
                else:
                    # messages.success(
                    #     request, "You have successfully logged in")
                    return redirect("student-dashboard-home")
            else:
                messages.warning(
                    request, "Your Username and Password doesn't match")
                return render(request, 'account/login.html')
        elif (username != "" and password != ""):
            return redirect("student-home")
    else:
        return render(request, 'account/login.html')


def signout(request):
    logout(request)
    return redirect('archive-home')
