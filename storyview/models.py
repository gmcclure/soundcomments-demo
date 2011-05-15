from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "stories"

    def __unicode__(self):
        return self.title[:20]
