from django.test import SimpleTestCase
from django.urls import reverse, resolve
from games.views import (
    GamesListView, GamesCreateView, OrganisationCreateView, GamesDetailView,
    PublisherDetailView, CategoryDetailView, OrganisationUpdateView, GameUpdateView
)

class TestGameUrls(SimpleTestCase):
    '''
    TEST_ASSETS_DIR contains external required content for test.
    Test func naming: test_<name of url>_url_is_resolved
    for ex if url is: path("<str:username>/", UserProfileView.as_view(), name="profile"),
    then: test_profile_url_is_resolved
    '''
    
    def test_games_list_url_is_resolved(self):
        url = reverse('games:games')
        self.assertEqual(resolve(url).func.view_class, GamesListView)

    def test_game_create_url_is_resolved(self):
        url = reverse('games:gamecreate')
        self.assertEqual(resolve(url).func.view_class, GamesCreateView)

    def test_organisation_create_url_is_resolved(self):
        url = reverse('games:organisationcreate')
        self.assertEqual(resolve(url).func.view_class, OrganisationCreateView)

    def test_game_detail_url_is_resolved(self):
        url = reverse('games:gamedetail', args=[1])
        self.assertEqual(resolve(url).func.view_class, GamesDetailView)

    def test_game_update_url_is_resolved(self):
        url = reverse('games:gameupdate', args=[1])
        self.assertEqual(resolve(url).func.view_class, GameUpdateView)

    def test_publisher_detail_url_is_resolved(self):
        url = reverse('games:publisherdetail', args=['someuser'])
        self.assertEqual(resolve(url).func.view_class, PublisherDetailView)

    def test_organisation_update_url_is_resolved(self):
        url = reverse('games:organisationupdate', args=['someuser'])
        self.assertEqual(resolve(url).func.view_class, OrganisationUpdateView)

    def test_category_detail_url_is_resolved(self):
        url = reverse('games:categorydetail', args=['somename'])
        self.assertEqual(resolve(url).func.view_class, CategoryDetailView)
