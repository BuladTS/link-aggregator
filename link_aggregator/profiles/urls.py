from django.urls import path

urlpattern = [
    path("profile/<slug:name>/", views.ProfileDetail, name="profile-detail")
]