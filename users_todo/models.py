from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UsersTodoList(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()
    on_priority = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    completed_at= models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)