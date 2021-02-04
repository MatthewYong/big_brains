from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A model to let users check their order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_email_address = models.CharField(max_length=50, null=False, blank=False)



