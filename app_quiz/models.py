from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=255)
    op1 = models.CharField(max_length=24)
    op2 = models.CharField(max_length=24)
    op3 = models.CharField(max_length=24)
    op4 = models.CharField(max_length=24)
    corr_ans = models.CharField(max_length=24)

    class Meta:
        db_table = "question"

    def __str__(self):
        return "%s" % self.question


class Duration(models.Model):
    time_in_minutes = models.IntegerField()

    class Meta:
        db_table = "duration"

    def __str__(self):
        return "%s" % self.time_in_minutes
