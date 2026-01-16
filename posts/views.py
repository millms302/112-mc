from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    """
    PostListView is going to retrieve all of the objexts from the Post table in db
    """

    # template_name attribute is going to render a specific HTML file
    template_name = "posts/list.html"
    # model is going to be from which table we want to retrieve the data
    model = Post
    # context_object_name allows us to modifyt the name on how we call it in the HTMLS
    context_object_name = "posts"

class PostDetailView(DetailView): # GET Method
    """
    PostDetailView is going to retriece a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView):
    """
    PostCreateView is going to allow us to create a new post and add it to the db
    """

    template_name = "posts/new.html"
    model = Post
    # Fields attribute allows us to control which elements to display on the form to create a new object
    # The name of the fields have to match with the attributes of the model.
    fields = ["title", "subtitle", "body"] 

class PostUpdateView(UpdateView):
    """
    """

    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    """
    Docstring for PostDeleteView
    """

    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")