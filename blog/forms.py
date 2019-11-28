from django import forms
from .models import Post

class PostForm(forms.ModelForm): #PostForm이라는 폼을 만들고 이 폼은 ModelForm이다
    class Meta: # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문.
        model = Post
        fields = ('title', 'text',)