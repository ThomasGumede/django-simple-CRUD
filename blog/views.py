from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post

class BlogListView(ListView):
    model = Post
    context_object_name = 'list'
    # paginate_by = 5
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'details'
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
