from django.urls import path
from App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('donate/', views.donate, name='donate'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('category/<str:category>/', views.category, name='category'),
]