from django.db import models

# Create your models here.

class calmodel(models.Model):
    name=models.CharField( max_length=50)
    quantity= models.FloatField()
    protien=models.FloatField()
    carbs=models.FloatField()
    fat=models.FloatField()
    nutrients=models.FloatField()
    vitamins= models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media',blank=True)
    def __str__(self):
        return (self.name)
    
class dropdo(models.Model):
    consumedfood = models.ForeignKey(calmodel,on_delete=models.CASCADE)
    quantity= models.FloatField()
    
class finalmodel(models.Model):
    name=models.CharField( max_length=50)
    quantity= models.FloatField()
    protien=models.FloatField()
    carbs=models.FloatField()
    fat=models.FloatField()
    nutrients=models.FloatField()
    vitamins= models.CharField(max_length=50)
    def __str__(self):
        return (self.name)