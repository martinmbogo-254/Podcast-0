from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm ,ProfileUpdateForm, UserUpdateForm


def register(request):
    #redirect a user to the homepage if they are already loged in
    if request.user.is_authenticated:
        return redirect('home')
    else:
        #perform this operation if the user is not logged in
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Hello {username}, Your account has been successfully created.. !! You can now login ')
                return redirect('login')
        else:
            form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        #show the current user details
        u_form = UserUpdateForm(request.POST, instance=request.user, )
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} Your profile has been successfully updated !!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user, )
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)
