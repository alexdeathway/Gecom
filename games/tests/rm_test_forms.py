from django.test import TestCase, Client
from django.urls import reverse
from games.models import GamesModel, OrganisationModel
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
import os

User = get_user_model()

class TestForms(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.organisation_data = {
            'name': 'Blend Studios',
            'username': 'blendstudios',
            'email': 'contact@blendstudios.com',
            'owner':self.user
        }

        self.game_data = {
            'name': 'Days Gone',
            'category': 'Action-Adventure', 
            'cover': SimpleUploadedFile(name='test_cover.jpg', content=b'cover_image_data', content_type='image/jpeg'),
            'price': 20,
            'sale': True,
            'description': 'Days Gone is a third-person action-adventure game set in a post-apocalyptic open world. The player controls Deacon St. John, an outlaw-turned-drifter-bounty-hunter who prefers life on the road to wilderness encampments.',
            'publisher': "Sony Interactive Entertainment",  
        }

    def test_OrganisationCreationForm_object_creation(self):
        url = reverse('games:organisationcreate')
        get_response = self.client.get(url)
        self.organisation_data['csrfmiddlewaretoken'] = get_response.context['csrf_token']
        post_response = self.client.post(url, data=self.organisation_data)

        self.assertEqual(post_response.status_code, 302)  # Expecting redirect after successful creation

    def test_OrganisationUpdateForm_object_update(self):
        # Create an initial organization instance
        organisation = OrganisationModel.objects.create(
            name='Naughty dog',
            username='naughtydog', 
            email='contact@naughtydog.com',
            owner=self.user
        )

        url = reverse('games:organisationupdate', kwargs={'pk': organisation.pk})
        get_response = self.client.get(url)

        # Prepare updated data based on the existing organization data
        updated_data = self.organisation_data.copy()
        updated_data['name'] = 'Bend Studios Updated'
        updated_data['csrfmiddlewaretoken'] = get_response.context['csrf_token']
        
        # Send POST request to update the organization
        post_response = self.client.post(url, data=updated_data)

        # Assert the response is a redirect (HTTP 302) after successful update
        self.assertEqual(post_response.status_code, 302)

        # Refresh the instance from the database to check for updates
        organisation.refresh_from_db()  # Ensure we have the latest data from the DB
        self.assertEqual(organisation.name, 'Bend Studios Updated')  # Verify the name was updated

        
    def test_username_validation_in_organisation_creation(self):
        url = reverse('games:organisationcreate')
        get_response = self.client.get(url)
        
        bad_data = self.organisation_data.copy()
        bad_data['username'] = 'InvalidUsername!'  # Invalid username

        bad_data['csrfmiddlewaretoken'] = get_response.context['csrf_token']
        post_response = self.client.post(url, data=bad_data)

        self.assertContains(post_response, 'Sorry , username can contain only lower case alphabets and numbers' in post_response.content.decode())

    

    def test_OrganisationUpdateForm_username_validation(self):
        org = OrganisationModel.objects.create(**self.organisation_data, owner=self.user)
        url = reverse('games:organisationupdate', kwargs={'username': org.username})
        get_response = self.client.get(url)
        
        bad_data = self.organisation_data.copy()
        bad_data['username'] = 'InvalidUsername!'  # Invalid username

        bad_data['csrfmiddlewaretoken'] = get_response.context['csrf_token']
        post_response = self.client.post(url, data=bad_data)

        self.assertContains(post_response, 'Sorry , username can contain only lower case alphabets and numbers')

    def test_GameCreationForm_object_creation(self):
        url = reverse('games:gamecreate')
        get_response = self.client.get(url)
        self.game_data['csrfmiddlewaretoken'] = get_response.context['csrf_token']
        post_response = self.client.post(url, data=self.game_data)

        self.assertEqual(post_response.status_code, 302)  # Expecting redirect after successful creation

    def test_GameUpdateForm_object_update(self):

        game = GamesModel.objects.create(
            name='The Last of Us',
            category='Action-Adventure',
            cover= SimpleUploadedFile(name='test_cover.jpg', content=b'cover_image_data', content_type='image/jpeg'),
            price=30,
            sale=True,
            description='The Last of Us is a 2013 action-adventure game developed by Naughty Dog and published by Sony Computer Entertainment. Players control Joel, a smuggler tasked with escorting a teenage girl, Ellie, across a post-apocalyptic United States. The Last of Us is played from a third-person perspective.',
            publisher='Sony Computer Entertainment'
        )
        url = reverse('games:gameupdate', kwargs={'pk': game.pk})
        get_response = self.client.get(url)

        updated_data = self.game_data.copy()
        updated_data['name'] = 'Updated Game Name'  # Change the name for the update
        updated_data['csrfmiddlewaretoken'] = get_response.context['csrf_token']
        post_response = self.client.post(url, data=updated_data)

        self.assertEqual(post_response.status_code, 302)  # Expecting redirect after successful update


    def tearDown(self):
        OrganisationModel.objects.all().delete()
        GamesModel.objects.all().delete()
