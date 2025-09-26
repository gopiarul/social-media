# urls.py
from django.urls import path
from .views import PostListView, PostCreateView,PostDeleteView,PostUpdateView
app_name = "posts"  

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('crear/', PostCreateView.as_view(), name='crear_post'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
]
