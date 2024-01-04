from django.core.management.base import BaseCommand
from posts.models import Post


class Command(BaseCommand):
    help = 'update statistics (such as like, view) of posts'

    def handle(self, *args, **kwargs):
        Post.objects.all().update(views=100)
        self.stdout.write('----------- update statistics done successfully -----------')
