from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone

def blog_list(request):
    query = request.GET.get("q")
    if query:
        blogs = Blog.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        created_by = request.POST['created_by']
        Blog.objects.create(title=title, description=description, created_by=created_by, created_at=timezone.now())
        return redirect('blog_list')
    return render(request, 'blog_form.html')

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.description = request.POST['description']
        blog.created_by = request.POST['created_by']
        blog.save()
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'blog_form.html', {'blog': blog})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog_list')