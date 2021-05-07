from django.shortcuts import render
from datetime import datetime
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
   
    
    return render(request, 'blog/index.html', {'posts': posts})



def show(request, id):
    posts = Post.objects.get(id=id)
   
    return render(request,'blog/show.html', {'post' : posts}) 