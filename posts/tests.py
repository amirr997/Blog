from django.test import TestCase
from model_bakery import baker
from .models import Post
from .views import OthersPosts
from django.urls import reverse
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory


class TestPost(TestCase):
    def setUp(self):
        self.user = baker.make('auth.User')
        self.profile = baker.make('users.Profile', user=self.user)
        self.post = baker.make(Post, title='title_one', _quantity=2)

    def test_one(self):
        post_count = Post.objects.all().count()
        self.assertEqual(post_count, 2)

    def test_other_posts(self):
        url = reverse("others-posts")

        factory = APIRequestFactory()
        view = OthersPosts.as_view()
        request = factory.get(url)
        # force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.data[0]['title'], 'title_one')
