from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def allblogs(request):
    blogs = models.Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(models.Blog, pk = blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})