from django.urls import path
from Admin import views

urlpatterns = [
    path('', views.admin_index, name="admin"),

    path('authors/', views.authors, name="admin-authors"),
    path('add/authors/', views.add_authors, name="admin-add-authors"),
    path('edit/authors/<int:id>', views.edit_authors, name="admin-edit-authors"),
    path('delete/authors/<str:id>/', views.delete_authors, name="admin_delete_authors"),

    path('books/', views.books, name="admin-books"),
    path('add/books/', views.add_books, name="admin-add-books"),
    path('edit/books/<int:id>', views.edit_books, name="admin-edit-books"),
    path('delete/books/<str:id>/', views.delete_books, name="admin_delete_books"),

    path('categorys/', views.categorys, name="admin-categorys"),
    path('add/categorys/', views.add_categorys, name="admin-add-categorys"),
    path('edit/categorys/<int:id>', views.edit_categorys, name="admin-edit-categorys"),
    path('delete/categorys/<str:id>/', views.delete_categorys, name="admin_delete_categorys"),

    path('newsletter/', views.newsletter, name="admin-newsletter"),
    path('delete/newsletter/<int:id>', views.delete_newsletters, name="admin_delete_newsletter")

    # path('logout/', views.logout, name="logout"),
]