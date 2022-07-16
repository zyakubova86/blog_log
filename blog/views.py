from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "post_list.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ['title', 'description', 'body', 'img', 'author', ]

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={"pk": self.object.pk})


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title', 'description', 'body', 'img', 'author', ]

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('post_list')


class AboutPageView(TemplateView):
    template_name = "about.html"