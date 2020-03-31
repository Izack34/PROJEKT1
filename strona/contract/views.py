from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .forms import ContractForm, OfferForm
from .models import Request, Offer, Contract, Message
from blog.models import Post
# from users.models import Profile


@login_required
def contract_manager(request):
    form = ContractForm(request.POST)
    return render(request, 'contract/create_contract.html', {'form': form})


@login_required
def contract_list(request):
    pass


@login_required
def offer_manager(request, id=None):
    if id is None:
        user_id = request.POST.get("user-id")
        executor = User.objects.get(id=user_id)
        form = OfferForm(request.user, user_id, initial={'executor': executor})
    else:
        offer = Offer.objects.get(id=id)
        if ((request.user.id == offer.executor.id) or
                (request.user.id == offer.client.id)):
            user_id = offer.executor.id
            form = OfferForm(offer.client, user_id,
                             initial={'executor': User.objects.get(id=user_id),
                                      'price': offer.price,
                                      'deadline': offer.deadline,
                                      'description': offer.description,
                                      'post': offer.post,
                                      'offer_id': offer.id
                                      })
            return render(request, 'contract/make_offer.html', {'form': form,
                                                                'offer': offer
                                                                })
        else:
            return HttpResponseForbidden()
    return render(request, 'contract/make_offer.html', {'form': form})


@login_required
def offer_list(request):
    offers = (Offer.objects.filter(executor=request.user) |
              Offer.objects.filter(client=request.user))
    return render(request, 'contract/offer_list.html', {'offers': offers})


@login_required
def make_request(request):
    if request.method == "POST":
        post = Post.objects.get(id=request.POST.get("post-id", ""))
        # already_applicate decorator
        already_applicated = False
        for r in post.request_set.all():
            if r.applicant == request.user:
                already_applicated = True
        # end
        if post.author != request.user and not already_applicated:
            aplic = Request(post=post, applicant=request.user)
            aplic.save()
    return redirect("blog-home")


@login_required
def make_offer(request):
    # 3 check if user has rights to manage this offer
    if request.method == "POST":
        if request.POST.get("make") is not None:
            post = request.POST.get("post", "")
            executor = request.POST.get("executor", "")
            offer = Offer(post=Post.objects.get(id=post),
                          price=request.POST.get("price", ""),
                          description=request.POST.get("description", ""),
                          deadline=request.POST.get("deadline", ""),
                          client=request.user,
                          executor=User.objects.get(id=executor),
                          status="sent")

            message = Message(sender=request.user, to=offer.executor,
                              text="You have new offer",
                              offer=offer, m_type="green")
            offer.save()
            message.save()
        elif request.POST.get("apply") is not None:
            offer = Offer.objects.get(id=request.POST.get("offer_id", ""))
            offer.status = "applied"
            message = Message(sender=request.user, to=offer.client,
                              text="You offer is applied",
                              offer=offer, m_type="green")
            message.save()
            offer.save()
        elif request.POST.get("resend") is not None:
            offer = Offer.objects.get(id=request.POST.get("offer_id", ""))
            offer.status = "resended"
            if request.user == offer.client:
                sender = offer.client
                to = offer.executor
            else:
                sender = offer.executor
                to = offer.client
            message = Message(sender=sender, to=to,
                              text="You offer is changed",
                              offer=offer, m_type="yellow")
            message.save()
            offer.save()
        elif request.POST.get("reject") is not None:
            offer = Offer.objects.get(id=request.POST.get("offer_id", ""))
            if request.user == offer.client:
                sender = offer.client
                to = offer.executor
            else:
                sender = offer.executor
                to = offer.client
            message = Message(sender=sender, to=to,
                              text="You offer is rejected",
                              offer=None, m_type="red")
            message.save()
            offer.delete()
        elif request.POST.get("approve") is not None:
            offer = Offer.objects.get(id=request.POST.get("offer_id", ""))
            offer.status = "approved"
            contract = Contract(offer=offer, status="active")
            message = Message(sender=request.user, to=offer.executor,
                              text="You offer is approved",
                              offer=offer, m_type="green")
            message.save()
            post = offer.post
            for req in post.request_set.all():
                message = Message(sender=request.user, to=req.applicant,
                                  text="Post " + post.title + " is closed",
                                  offer=None, m_type="red")
                message.save()
            for single_offer in post.offer_set.all():
                if single_offer != offer:
                    single_offer.delete()
            offer.save()
            post.delete()
            contract.save()
    return redirect("blog-home")


@login_required
def inbox(request):
    messages = Message.objects.filter(to=request.user)
    return render(request, "contract/inbox.html",
                  {'custom_messages': messages})


@login_required
def delete_message(request):
    if request.method == "POST":
        message_id = request.POST.get("message_id", "")
        message = Message.objects.get(id=message_id)
        message.delete()
    return redirect("inbox")
