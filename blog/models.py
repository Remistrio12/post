from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return str(self.title)
    class META:
        verbose_name_plural = 'post'

