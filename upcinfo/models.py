from django.db import models

class UPCProduct(models.Model):
    prodid = models.BigIntegerField()
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField()
    extra_fields = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title