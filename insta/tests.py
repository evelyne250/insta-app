from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='eve')
        self.user.save()

        self.profile_test = Profile( profile_picture='insta.jpg', bio='this is a test profile', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        travel = Profile.objects.all()

    def tearDown(self):
        '''
        Test delete category behaivour
        
        '''
        Profile.objects.all().delete()
        

    def test_delete_profile(self):
        '''
        Test if category can be deleted from db.
        '''
        self.save_profile()
        self.profile = Profile.objects.get(id = 1)
        self.profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)

class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile()
        self.profile_test.save()

        self.image_test = Image(image='insta.png', image_name='test', caption='default test', profile=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        '''
        Test delete category behaivour
        
        '''
        Image.objects.all().delete()
        

    def test_delete_image(self):
        '''
        Test if category can be deleted from db.
        '''
        self.images.save_image()
        self.image = Image.objects.get(id = 1)
        self.image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)