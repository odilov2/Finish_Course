from django.shortcuts import render, redirect
from django.views import View
from .models import Users, Teams
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, RegisterForm


class UsersView(View):
    def get(self, request):
        users = Users.objects.all()
        return render(request, 'register.html', {'users': users})


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {'username': username, 'password': password}
        login_form = AuthenticationForm(data=data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

        else:
            context = {'form': login_form}
            return render(request, 'index.html', context)


class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password
        }
        create_user = RegisterForm(data=data)
        if create_user.is_valid():
            # create_user.save()
            return redirect('login')
        else:
            context = {'form': create_user}
            return render(request, 'register.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


