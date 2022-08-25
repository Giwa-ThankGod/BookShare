from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from App.models import *

# Create your models here.
class Activity(models.Model):
    description = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender = Author)
    def author_activity(sender, instance, created, **kwargs):
        if created:
            Activity.objects.create(description = 'New Author Added : {}'.format(instance.name)).save()

    @receiver(post_save, sender = Book)
    def book_activity(sender, instance, created, **kwargs):
        if created:
            Activity.objects.create(description = 'New Book Added : {}'.format(instance.title)).save()

    @receiver(post_save, sender = Category)
    def category_activity(sender, instance, created, **kwargs):
        if created:
            Activity.objects.create(description = 'New Category Added : {}'.format(instance.name)).save()