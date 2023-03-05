from django.db import models


class Complaint(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True, default='')
	complaint = models.TextField(blank=False, null=False)
	sentiment = models.CharField(verbose_name='sentiment category',
                                blank=True, null=True, max_length=20)
	date = models.DateTimeField(auto_now_add=True)