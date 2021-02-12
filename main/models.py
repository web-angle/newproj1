from django.db import models


# Create your models here.
class Data(models.Model):
	code = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.code


class Data_new(models.Model):
	access_token = models.CharField(max_length=200, null=True, blank=True)
	fresh_token = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.access_token
