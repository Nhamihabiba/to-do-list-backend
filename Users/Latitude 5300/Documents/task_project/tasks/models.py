from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
