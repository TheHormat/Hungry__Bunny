from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=120, null=True)
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='modified_by')

    slug = models.SlugField(unique=True, max_length=120, editable=False)
    
    def __str__(self):
        return f'{self.title}'

    def get_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique = slug
        number = 1

        while Post.objects.filter(slug=unique).exists():
            unique = f'{slug}-{number}'
            number += 1
        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    gmail = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
