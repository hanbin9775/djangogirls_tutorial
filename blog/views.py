from django.shortcuts import render

# Create your views here.

# 요청을 넘겨받아 render를 호출. 이 함수는 render 메서드를 호출하여 받은 blog/post_list.html 템플릿을 보여준다
def post_list(request):
    return render(request, 'blog/post_list.html',{})