from django.db import models

class Question(models.Model):
    """
    Model for Questions table in our DB
    """
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    """
    Model for choices based on the Question table / model
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
