from django.shortcuts import render, redirect, resolve_url
from . import views
from .forms import PostForm
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html',{'posts':posts})
    
def create(request):
    if request.method == 'POST':
        #저장로직
        form = PostForm(request.POST) # 입력했던 title, content가 request.POST안에 들어가있음
        if form.is_valid(): #규칙이 어긋나는지 검증하는 과정
            title = form.cleaned_data['title']
            # title = form.cleaned_data.get('title')
            content = form.cleaned_data['content']
            Post.objects.create(title=title, content=content)
        
            return redirect(resolve_url('post:list'))
        
        
    else:
        form = PostForm() #html코드로 바꿔주는애
    return render(request, 'post/create.html', {'form':form})


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/detail.html',{'post':post})
    
    
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(resolve_url('post:list'))
    
def update(request, id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            # post.update(title=title, content=content)
            post.save()
            return redirect(resolve_url('post:detail', id))
    
    else:
        form = PostForm({'title':post.title,'content':post.content})
        return render(request, 'post/update.html',{'form':form,'post':post})