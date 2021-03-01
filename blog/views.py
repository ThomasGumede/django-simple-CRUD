from django.views.generic import ListView, DetailView
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
