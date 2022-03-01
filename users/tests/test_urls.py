from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse,resolve
from users.views import UserProfileView,UserProfileUpdateView
import os, random, string 

User=get_user_model()

def dummy_password():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class TestUrl(TestCase):

    
    def setUp(self):
        '''
        
        TEST_ASSETS_DIR contains external required content for test. 
        
        Test func naming: test_<name of url>_url_is_resolved
        for ex if url is:path("<str:username>/",UserProfileView.as_view(),name="profile"),,
                    then:  test_profile_url_is_resolved
        
        '''

        self.TEST_ASSETS_DIR=os.path.join(settings.BASE_DIR,'test_assets')

        #dummy user data will be used to create and login during the test session 
        self.user_dummy_username='testuser'
        self.user_dummy_password=dummy_password()
        self.client=Client()    
        self.user = User.objects.create_user(username=self.user_dummy_username, password=self.user_dummy_password)
        self.client.login(username=self.user_dummy_username,password=self.user_dummy_password)        

    def test_profile_url_is_resolved(self):
        url=reverse('users:profile',args=[self.user_dummy_username])
        
        self.assertEqual(resolve(url).func.view_class,UserProfileView)

    
    def test_profileupdate_url_is_resolved(self):
        url=reverse('users:profileupdate',args=[self.user_dummy_username])
        
        self.assertEqual(resolve(url).func.view_class,UserProfileUpdateView)    

