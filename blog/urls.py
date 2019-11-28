from django.urls import path
from . import views


urlpatterns = [
    #장고에게 누군가 웹사이트 홈 주소로 들어왔을 때 views.post_list를 보여주라고 말해준다.
    path('', views.post_list, name='post_list'), #name은 url에 이름을 붙인 것으로 뷰를 식별한다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #<int:pk> : pk값으로 정수 값을 보낸다는 의미
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]



