from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView

import re
from pytube import YouTube

from download.forms import *


class HomePage(FormView):
    form_class = FindForm
    template_name = 'download/index.html'
    extra_context = {'title': 'Download vidio from YouTube'}

    def form_valid(self, form):
        if not "https://www.youtube.com/watch" in form.cleaned_data['link']:
            return redirect('home')
        return redirect(f'/load&{re.findall(r"v=([A-Za-z0-9_-]+)", form.cleaned_data["link"])[0]}')


class LoadVideo(TemplateView):
    template_name = 'download/load.html'
    extra_context = {'title': 'Download video'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = self.request.build_absolute_uri()
        yt = YouTube(f'http://youtube.com/watch?v={url.split("&")[-1]}', use_oauth=True, allow_oauth_cache=True)
        context['title_video'] = yt.title
        context['url_video'] = yt.thumbnail_url
        strm = yt.streams.filter(res="720p")
        strm.first().download(output_path="download/static/download/video", filename="video.mp4")
        return context