from pyexpat import model
from django.contrib import admin
from App.models import *

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author

class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book

admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Newsletter)