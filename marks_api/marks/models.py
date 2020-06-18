from django.db import models

# Create your models here.
class Mark(models.Model):
    name = models.CharField(max_length=64, default='unnamed')
    latti = models.FloatField(null=False, blank=False)
    longi = models.FloatField(null=False, blank=False)
    author = models.CharField(max_length=64, default='???')
    addrdate = models.CharField(max_length=64, null=False, blank=False)
    photo = models.URLField(max_length=200, null=False, blank=False)
    status = models.CharField(max_length=10, default='onspot', null=False, blank=False)
    typeof = models.CharField(max_length=10, default='graffity', null=False, blank=False)

    def __str__(self):
        return f'{self.name} by {self.author}'
