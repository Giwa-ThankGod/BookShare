from django.urls import path
from Paystack import views 

urlpatterns = [
    path('', views.initiate_payment, name="initiate-payment"),
    path('verify-payment/<str:ref>', views.verify_payment, name="verify-payment")
]