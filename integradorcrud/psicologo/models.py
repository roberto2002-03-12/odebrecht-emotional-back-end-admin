from django.db import models

# Create your models here.

class professional(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.first_name), filename])
    
    email = models.CharField(max_length=65)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    local_number = models.IntegerField()
    licensed = models.CharField(max_length=35)
    address = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to=nameFile, null=True, blank=True)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=35)

    class Meta:
        db_table = "professional"