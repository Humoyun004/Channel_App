from django.shortcuts import render

from .models import Poster

# Create your views here.
def home(request):
    return render(request, 'posts/index.html')

def channel(request):
    posts = Poster.objects.all()
    return render(request, 'posts/channel.html',context={'posts':posts})