from django.db import models

class TimeStampedModel(models.Model):
    """
    생성 시간과 수정 시간을 자동으로 업데이트해 주는 추상화 기반 클래스 모델
    """
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True     # 추상화 기초 클래스로 선언 => migration시 테이블 생성X


class CostModel(TimeStampedModel):

    date = models.DateField()
    tag = models.CharField(max_length=30)
    price = models.IntegerField()
    content = models.CharField(max_length=100)
    contain = models.BooleanField(verbose_name="계산시 포함 여부")
    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-date']