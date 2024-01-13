from django.shortcuts import render

# Create your views here.
def reels(request):
    return render(request, 'reels/reels.html')


def reels_view(request):
    return render(request, 'reels/reels_view.html')