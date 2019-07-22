from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
