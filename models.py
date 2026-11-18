from django.db import models
from django.contrib.auth.models import User

class Laver(models.TextChoices):
    MY_PAGE = 'my_page', 'Моя страница'
    WORK = 'work', 'Работа'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    page_type = models.CharField(max_length=50, choices=Laver.choices, default=Laver.MY_PAGE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
