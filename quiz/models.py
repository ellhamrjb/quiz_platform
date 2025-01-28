from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text=models.CharField(max_length=255)
    correct_answer=models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
class UserScore(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.score}"
