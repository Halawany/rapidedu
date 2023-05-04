from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        # Save the user to the database
        response = super().form_valid(form)
        form.save()

        # Authenticate the user and log them in
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return response

class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        kwargs['form_type'] = 'login'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class LogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('login')