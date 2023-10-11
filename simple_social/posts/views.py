#posts/views.py

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin # braces is needed to be installed. pip install django-braces

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    """
    shows a list of the posts related to either the user or the group or both of them
    """
    model = models.Post
    select_related = ("user", "group") # this is a tuple of related models. The users the post belons to and group the post belongs to. Or in other words, the foreign key ForeignKey the post .
    queryset=models.Post.objects.all()


    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args,**kwargs)

        if self.request.user.is_authenticated:
            context['get_user_groups'] = models.Group.objects.filter(members__in=[self.request.user])

        context['get_other_groups'] = models.Group.objects.all()

#
class UserPosts(generic.ListView):
    """
    Posts of currently logged in user
    """
    model = models.Post
    template_name = "posts/user_post_list.html" #this is not a default name of the teplate, so we specify it here:
    #If you use default template names such as post_list.html (here, you have a models class named Post) then you don't need to write a template name. But your template name is post_data_list.html, you must need template_name variable.
#
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
#
    def get_context_data(self, **kwargs):
        """
        Returning the context data object essentially connected to whoever actually posted
        """
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context
#
#
class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )
#
#
class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','group')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        """
        Connecting actual post to the user itself.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user# self.request is an attribute that holds information about the current HTTP request being processed, and self.request.user represents the currently authenticated user.
        self.object.save()
        return super().form_valid(form)
#
#
class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        """
        In summary, this code extends the default delete behavior for an object,
         and before performing the actual deletion, it adds a success message to
         the user indicating that the post has been deleted.
        """
        messages.success(self.request, "Post Deleted") #Messages are built into a Django project, and they add responsiveness to a website.
        return super().delete(*args, **kwargs)
