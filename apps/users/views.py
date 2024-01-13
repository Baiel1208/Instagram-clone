from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')


def profile(request):
    return render(request, 'users/profile.html')

def peaple(request):
    return render(request, 'users/peaple.html')


def setting(request):
    return render(request, 'users/setting.html')