from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'