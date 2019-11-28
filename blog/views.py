from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
#뷰는 장고 어플리케이션이 일반적으로 특정 기능과 템플릿을 제공하는 웹페이지의 한 종류이다.

# 요청을 넘겨받아 render를 호출. 이 함수는 render 메서드를 호출하여 받은 blog/post_list.html 템플릿을 보여준다
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts}) #post_list.html에 posts 값을 매개변수 posts에 전달

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        #method가 POST라면 폼에서 받은 데이터를 PostForm으로 넘겨준다.
        form = PostForm(request.POST)
        if form.is_valid():
            #넘겨진 데이터를 바로 저장하지는 말라 ( 작성자 추가 필요)
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #새로 작성한 글 볼 수 있도록 post_detail 페이지로 가라고 수정
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    #request에는 우리가 입력했던 데이터들을 가지고 있는데, request.POST가 이 데이터를 가지고 있다
    return render(request, 'blog/post_edit.html', {'form':form})