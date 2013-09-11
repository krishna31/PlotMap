from django.db import models

# Create your models here.
class location(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150) 
    lat = models.DecimalField(max_digits=12, decimal_places=8) 
    lang = models.DecimalField(max_digits=12, decimal_places=8)
    description = models.TextField(blank=True, null=True) 
    def __unicode__(self):
          return u'%s' % self.name
