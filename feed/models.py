from django.db import models
from django.contrib.auth.models import User

class Gop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link to Django user
    name = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profiles/", default="profiles/default.png")
    followers = models.ManyToManyField(User, related_name="gop_following", blank=True)

    def __str__(self):
        return self.name
