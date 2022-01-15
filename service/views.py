from django.shortcuts import render
from service.forms import PostForm
from .models import *


def index(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    else:
        form = PostForm()

    return render(request, "index.html", {"form": form})

def report(request):
    reports = Post.objects.all()
    context = {'reports': reports}
    return render(request, 'Report.html', context)
