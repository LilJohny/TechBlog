from django.conf.urls import url
from django.urls import path, include
from account.views import dashboard, register
import django.contrib.auth.urls

import social_django.urls
urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include(django.contrib.auth.urls)),
    path("register/", register, name="register"),
    url(r"^oauth/", include("social_django.urls")),
]
