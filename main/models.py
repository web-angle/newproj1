from django.db import models


class Data(models.Model):
	code = models.CharField(max_length=300, null=True, blank=True)
	access_token = models.TextField(null=True, blank=True)
	refresh_token = models.CharField(max_length=300, null=True, blank=True)
	token_type = models.CharField(max_length=200, null=True, blank=True)
	expires_in = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.code
