from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    question_text = models.CharField(max_length=255)
    choices = models.TextField()
    right_choice = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


