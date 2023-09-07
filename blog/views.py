from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from blog import models
from blog.models import Photo
from django.urls import reverse
from django.http import HttpResponseRedirect


@login_required
def like_photo(request, photo_id):
   pass


@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, "blog/home.html", context={"photos":photos})


@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})
