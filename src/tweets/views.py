from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
                                CreateView,
                                DetailView,
                                DeleteView,
                                ListView,
                                UpdateView
                                  )

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet


class TweetCreateView(LoginRequiredMixin,CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    #success_url = reverse_lazy("tweet:detail")


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse("tweet:list")  # reverse()


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args,**kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


def tweet_detail_view(request, pk=None):
    # obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)






























