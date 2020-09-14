from django.shortcuts import render
from django.views.generic import (TemplatesView, ListView)
from blog_app.models import Post, Comment


class AboutView(TemplatesView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))