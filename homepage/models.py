from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    # include rename function here, where Image name = title
    header_image = models.FileField(blank=True, upload_to='header_image/%Y/%m/%d/', max_length=200)  #file will be uploaded to MEDIA_ROOT/uploads/<year>/<month>/<day>
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    reference = models.URLField(blank=True, max_length=200)

    def __str__(self):
        return self.title