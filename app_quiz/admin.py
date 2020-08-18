from django.contrib import admin
from .models import Question, Duration

# Register your models here.

model_list = [Question, Duration]

admin.site.register(model_list)
