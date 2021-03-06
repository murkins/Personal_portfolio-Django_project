from django.shortcuts import render, get_object_or_404
from .models import ProjectBlog

def all_blogs(request):
    projects_blog = ProjectBlog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'projects_blog':projects_blog})

def detail(request, blog_id):
    blog = get_object_or_404(ProjectBlog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
