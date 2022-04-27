from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view),
    path("away/<str:sitelink>/", views.siteRedirect),
    path("suggest/", views.suggest)
]