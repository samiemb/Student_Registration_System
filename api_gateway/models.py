from django.db import models
from django.utils import timezone

class ApiRequestLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)  # Foreign key to User if available
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)  # e.g., GET, POST, etc.
    status_code = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.method} {self.endpoint} - Status {self.status_code}"


class ApiToken(models.Model):
    user_id = models.IntegerField(unique=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Token for User {self.user_id}"

