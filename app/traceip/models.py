from django.db import models

# Create your models here.
class TraceIp(models.Model):
	request_by_ip   = models.CharField(max_length=20, null=True, blank=True)
	searched_for_ip = models.CharField(max_length=20, null=True, blank=True)
	created_on 		= models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table  = 'Traceip'
		verbose_name_plural = 'Traceip'

	def __str__(self):
		return self.searched_for_ip