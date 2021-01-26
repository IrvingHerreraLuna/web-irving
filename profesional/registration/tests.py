from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@test.com','test12345')
        
    def test_profile_exist(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists,True)