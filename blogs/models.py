from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    date = models.CharField(max_length=20, null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    article = models.CharField(max_length=10000, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title