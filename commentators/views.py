from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import CustomUserCreationForm, EditProfileForm


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, "There Was An Error Logging In, Try Again...")
                return redirect('login')
        else:
            return render(request, 'login.html', {})


def logout_user(request):
    messages.success(request, "You logged out")
    logout(request)
    return redirect('home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                email = form.cleaned_data['email']
                user = authenticate(username=username, password=password, email=email)
                login(request, user)
                messages.success(request, ("Registration Successful!"))
                return redirect('home')
        else:
            form = CustomUserCreationForm()

        return render(request, 'register.html', {
            'form': form,
        })


class UserEditView(generic.UpdateView, LoginRequiredMixin):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


