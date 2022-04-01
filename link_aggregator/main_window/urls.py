from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('registrations', views.registrations, name='registrations'),
    path('authorization', views.authorization, name='authorization'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
