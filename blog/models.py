from django.conf import settings
from django.db import models
from django.utils import timezone

#models : 장고 모델임을 의미. 이 코드 때문에 장고는 post가 데이터베이스에 저장되어야 한다고 알게 됨.
class Post(models.Model):
    #속성
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #다른 모델에 대한 링크 의미
    title = models.CharField(max_length=200) # 글자 수가 제한된 텍스트 정의할 때
    text = models.TextField() # 글자 수에 제한이 없는 긴 텍스트
    created_date = models.DateTimeField( # 날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField( 
            blank=True, null=True)

    #메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title