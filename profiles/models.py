from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    A model to let users check their order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_email_address = models.CharField(
                        max_length=50, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofiel.save()
