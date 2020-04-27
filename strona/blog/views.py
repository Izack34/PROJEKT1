from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from taggit.models import Tag


def home(request):  
    context= {
        'tags': Tag.objects.all(),
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=10

class FindListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=10
    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Post.objects.filter(Q(title__icontains=query)| Q(content__icontains=query)).order_by('-date_posted')
        return results
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=10

    def get_queryset(self):
        user =get_object_or_404(User, username =self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class TagListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=10
    def get_queryset(self):
        #tag = get_object_or_404(Tag, slug==self.kwargs.get('slug'))
        return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-date_posted')
        


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['title','content','expire_date','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title','content','expire_date','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
