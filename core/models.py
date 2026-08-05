from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    email3 = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AlertHistory(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    message = models.TextField()
    location_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert by {self.user.name} at {self.created_at:%Y-%m-%d %H:%M}"


# Create your models here.
