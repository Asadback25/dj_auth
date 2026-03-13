from django.shortcuts import render , redirect
from .forms import ProfileForm , UserForm
from django.contrib.auth.forms import PasswordChangeForm

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {'form':form}
    return render(request,'profile_update.html',context)


def change_password(request):
    user = request.user
    form = PasswordChangeForm(user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user)
    context = {
        'form':form
    }
    return render(request,'change_password.html',context)


def profile(request):
    user = request.user
    context = {'user':user}
    return render(request,'profile.html',context)