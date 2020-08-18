from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return "%s" % self.name
