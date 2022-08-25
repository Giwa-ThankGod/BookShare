from Paystack.paystack import Paystack
import secrets # This is a django module that helps generate a unique token number
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    thumb = models.ImageField(upload_to='category', null=True, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.thumb.url
        except:
            url = ''
        
        return url

class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    ref = models.CharField(max_length=200, default='1000')
    cover = models.ImageField(upload_to='book', null=True) #blank=False
    category = models.ManyToManyField(Category, related_name='book')
    # related_name here helps me access Book instances from Category instance e.g category.book.count
    author = models.ForeignKey(Author, on_delete= models.CASCADE, null=True)

    class Meta:
        ordering = ['title'] #order the books in alphabetical order.

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50) #50 is the length of the ref
            object_with_similar_ref = Book.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    @property
    def imageUrl(self):
        try:
            url = self.cover.url
        except:
            url = ''
        
        return url

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email