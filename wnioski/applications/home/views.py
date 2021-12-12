from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    TemplateView,
    CreateView,
)
from applications.users.models import User

class HomePage(LoginRequiredMixin, TemplateView):
 
    template_name = "home/index.html"
    model =User
    # loginmixin wymaga żeby podać parametr co robić jeśli user is not 
    login_url = reverse_lazy('users_app:user-login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.role == 'S':
            context['show_director'] = True
        if self.request.user.role == 'K' or self.request.user.role == 'T':
            context['show_manager'] = True
        return context

   