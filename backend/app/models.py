from django.db import models

class UserState(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    state = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"User {self.chat_id} - {self.state}"
    