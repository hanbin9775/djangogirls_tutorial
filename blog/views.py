from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
#뷰는 장고 어플리케이션이 일반적으로 특정 기능과 템플릿을 제공하는 웹페이지의 한 종류이다.

# 요청을 넘겨받아 render를 호출. 이 함수는 render 메서드를 호출하여 받은 blog/post_list.html 템플릿을 보여준다
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts}) #post_list.html에 posts 값을 매개변수 posts에 전달