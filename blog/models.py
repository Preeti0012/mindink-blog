from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    def __str__(self):
        return self.title


