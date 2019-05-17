from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class NewManager(models.Manager):
    def get_queryset(self):
        return super(NewManager, self).get_queryset().filter(status="new")

# Create your models here.
class Post(models.Model):
    objects = models.Manager()                  #Our default Manager
    new = NewManager()                          #Our Custom Model Manager

    STATUS_CHOICES = (
        ('vocabulary','Vocabulary'),
        ('test','Test'),
        ('new','New'),

    )

    title       =       models.CharField(max_length = 100)
    slug        =       models.SlugField(max_length = 120)
    author      =       models.ForeignKey(User, related_name = 'blog_posts')
    body        =       models.TextField()
    likes       =       models.ManyToManyField(User, related_name='likes', blank=True)
    created     =       models.DateTimeField(auto_now_add=True)
    updated     =       models.DateTimeField(auto_now_add=True)
    status      =       models.CharField(max_length = 10, choices= STATUS_CHOICES, default='new')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


    def total_likes(self):
        return self.likes.count()


    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id, self.slug])

@receiver(pre_save, sender=Post)    
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null= True, blank=True)
    photo = models.ImageField(null=True, blank=True)


    def __str__(self):
        return "Profile of user {}".format(self.user.username)



class Images(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title + " Image"