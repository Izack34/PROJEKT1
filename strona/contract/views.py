from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContractForm
from .models import Request
from blog.models import Post
from users.models import Profile


@login_required
def contract_manager(request):
   form = ContractForm(request.POST)
   return render(request, 'contract/create_contract.html', {'form':form})


@login_required
def contract_list(request):
    pass


@login_required
def offer_manager(request):
    pass


@login_required
def offer_list(request):
    pass


@login_required
def make_request(request):
    if request.method == "POST":
        post = Post.objects.get(id=request.POST.get("post-id", ""))
        if post.author != request.user:
            request = Request(post=post, applicant=request.user)
            request.save()
    return redirect("blog-home")
