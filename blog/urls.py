from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, AboutPageView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(BlogListView.as_view()), name="post_list"),
    path('about/', login_required(AboutPageView.as_view()), name="about"),
    path('post/<int:pk>/', login_required(BlogDetailView.as_view()), name="post_detail"),
    path('post/create/', login_required(BlogCreateView.as_view()), name="post_create"),
    path('post/<int:pk>/update', login_required(BlogUpdateView.as_view()), name="post_update"),
    path('post/<int:pk>/delete', login_required(BlogDeleteView.as_view()), name="post_delete"),
]

