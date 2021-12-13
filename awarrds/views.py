from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Rating
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login/')
def profile(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'profile.html', locals())

