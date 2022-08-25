from django.contrib import admin
from django.urls import path, include

#import for serving media files upload by user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('accounts/', include("django.contrib.auth.urls"), name="accounts"),
    path('dashboard/',include('Admin.urls'), name="dashboard"),
    path('',include('App.urls')),
    path('paystack/',include('Paystack.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
