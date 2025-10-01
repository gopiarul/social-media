from django.urls import path
from .views import feed, load_more
from.import views

urlpatterns = [
    path('', feed, name='feed'),
    path('load-more/', load_more, name='load_more'),
    path("follow/<int:gop_id>/", views.follow_toggle, name="follow_toggle"),
]
