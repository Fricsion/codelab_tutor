from django.db import models

class GptResponse(models.Model):
    user_input = models.TextField()
    gpt_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response from {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"