from django.urls import path
from . import views

#장고에게 누군가 웹사이트 홈 주소로 들어왔을 때 views.post_list를 보여주라고 말해준다.
urlpatterns = [
    path('', views.post_list, name='post_list'), #name은 url에 이름을 붙인 것으로 뷰를 식별한다.
]



