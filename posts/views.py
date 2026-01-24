from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )

class PostDraftListView(ListView):
    """
    PostDraftListView is going to help us to display all posts from the db with a Draft status
    """
    template_name = "posts/draft.html"
    context_object_name = "drafts"
    draft_status = Status.objects.get(name="Draft")
    queryset = Post.objects.filter(status=draft_status).order_by("created_on").reverse()
    


class PostArchivedListView(ListView):
    """
    PostArchivedListView is going to help us to display all posts from the db with a Archived status
    """
    template_name = "posts/archived.html"
    context_object_name = "archived"
    archived_status = Status.objects.get(name="Archived")
    queryset = Post.objects.filter(status=archived_status).order_by("created_on").reverse()

class PostListView(ListView):
    """
    PostListView is going to retrieve all of the objexts from the Post table in db
    """

    # template_name attribute is going to render a specific HTML file
    template_name = "posts/list.html"
    # model is going to be from which table we want to retrieve the data
    #model = Post
    published_status = Status.objects.get(name="Published")
    #Queryset attribute allow us to select some data from the db by using the model class
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    # context_object_name allows us to modifyt the name on how we call it in the HTMLS
    context_object_name = "posts"

class PostDetailView(LoginRequiredMixin, DetailView): # GET Method
    """
    PostDetailView is going to retriece a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    PostCreateView is going to allow us to create a new post and add it to the db
    """

    template_name = "posts/new.html"
    model = Post
    # Fields attribute allows us to control which elements to display on the form to create a new object
    # The name of the fields have to match with the attributes of the model.
    fields = ["title", "subtitle", "body", "status"] 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    """

    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated():
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Docstring for PostDeleteView
    """

    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated():
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False
