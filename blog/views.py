from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

# View a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Create a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'slug', 'author', 'content', 'status', 'image']
    success_url = reverse_lazy('post_list')

# Update an existing post
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'slug', 'author', 'content', 'status', 'image']
    success_url = reverse_lazy('post_list')

# Delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
class PostSearchView(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(slug__icontains=query, status=1)
        return Post.objects.none()