from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Scholarships(models.Model):
	"""Scholarships Model"""

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	end_date = models.DateField()
	amount = models.IntegerField()
	amount_type = models.CharField(max_length=60)
	about = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)