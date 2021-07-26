from django.db import models


class InstagramHashtag(models.Model):
    title = models.CharField(max_length=250, verbose_name='Хештег', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Хештег Instagram"
        verbose_name_plural = "Хештеги Instagram"
