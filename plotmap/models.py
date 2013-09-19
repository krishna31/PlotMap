from django.db import models

# Create your models here.
class path(models.Model):
	start=models.CharField(max_length=255)
	end=models.CharField(max_length=255)
	def __unicode__(self):
          return u'%s' % self.id
class location(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150) 
    lat = models.DecimalField(max_digits=12, decimal_places=8) 
    lang = models.DecimalField(max_digits=12, decimal_places=8)
    description = models.TextField(blank=True, null=True)
    pathid= models.ForeignKey(path,null=True, blank=True,related_name='pathid')	 
    def __unicode__(self):
          return u'%s' % self.name
