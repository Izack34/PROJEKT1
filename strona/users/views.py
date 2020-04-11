from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm, CommentForm
from .models import Profile,Comment

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created  for {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})



def view_profile(request, pk):
    profile_instance=Profile.objects.filter(user_id=pk).first()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.profile = profile_instance
            form.instance.author = request.user
            form.save()
            messages.success(request, 'comment created!')
            return redirect(f'/profile/{pk}')
    else:
        form = CommentForm()

    context= {
        'form': form,
        'u_profile': profile_instance,
        'comments': Comment.objects.filter(profile=profile_instance)
    }
    
    
    return render(request, 'users/profile.html', context)



@login_required
def my_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES ,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return  render(request, 'users/myprofile.html',context)



