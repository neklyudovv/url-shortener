from django.db import models

# Create your models here.
class url(models.Model):
	longUrl = models.TextField()
	shortUrl = models.TextField()

	def __str__(self):
		return self.longUrl