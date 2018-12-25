from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST': # if the request returned is a POST
        form = UserRegisterForm(request.POST) #we get the same info that we entered
        if form.is_valid(): #If form has valid fields.
            form.save()
            username = form.cleaned_data.get('username') #gets the username and converts the data to something readable
            messages.success(request, f'Your Account haas been created!') #If form data is valid
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required #Adds certain functionality to a function
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #The fields are current user
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                    instance=request.user.profile) #Field are current profile
        #Form has request.files because its getting extra data from files(pic).
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account haas been updated!') #If form data is valid
            return redirect('profile') #Prevents render template function call

    else:
        u_form = UserUpdateForm(instance=request.user) #The fields are current user
        p_form = ProfileUpdateForm(instance=request.user.profile) #Field are current profile

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
