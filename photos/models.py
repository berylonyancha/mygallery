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

lass Image(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image_url = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(categories__name__contains=search_term)
        if len(images) < 1:
            case_images = cls.objects.filter(
                categories__name__contains=search_term.capitalize())
            return case_images
        else:
            return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image
