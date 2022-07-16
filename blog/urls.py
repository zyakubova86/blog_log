from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', BlogListView.as_view(), name="post_list"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('post/create/', BlogCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name="post_delete"),

]

