from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'base/home.html')

def code(request):
     return render(request, 'code.html')

def components(request):
     return render(request, 'components.html')

def explore(request):
     return render(request, 'explore.html')

def messages(request):
     return render(request, 'messages.html')

def shop(request):
     return render(request, 'shop.html')

def upgrade(request):
     return render(request, 'upgrade.html')