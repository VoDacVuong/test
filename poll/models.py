from django.db import models

# Create your models here.

class Question(models.Model):
    question_tex = models.CharField(max_length=50)
    time = models.DateTimeField()

    def __str__(self):
        return self.question_tex
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=90)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    
