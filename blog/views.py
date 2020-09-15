from django.shortcuts import render, get_object_or_404
from .models import ProjectBlog

def myblog(request):
    blog_count = ProjectBlog.objects.count()
    projects = ProjectBlog.objects.order_by('-date')
    return render(request, 'blog/myblog.html', {'myblogproject': projects})

def details(request, blog_id):
    blogs = get_object_or_404(ProjectBlog, pk=blog_id)
    return render(request, 'blog/details.html', {'blogs': blogs})

