from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Post


class Command(BaseCommand):
    help = 'Deletes expired posts'

    def handle(self, *args, **options):
        now = timezone.now()
        Post.objects.filter(expire_date__lt=now).delete()