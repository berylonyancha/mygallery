from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Food')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save()

        self.category = Category(name='Food')
        self.category.save()

        self.girl = Image(title='girl',description='This is a test instance',location=self.location,category=self.category)
        self.girl.save_image()

        self.chapati = Image(title='chapati',description='This is the second test instance',location=self.location,category=self.category)
        self.chapati.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.girl,Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.girl.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.girl.save_image()
        self.girl.delete_image()
        self.chapati.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

  

    def test_get_image_by_id(self):
        found_image = self.girl.get_image_by_id(self.girl.id)
        image = Image.objects.filter(id=self.girl.id)
        self.assertTrue(found_image,image)

    def test_search_by_category(self):
        category = 'Food'
        found_image = self.girl.search_by_category(category)
        self.assertTrue(len(found_image)>1)