from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from blog import models
from blog.models import Photo, Comment
from django.urls import reverse
from django.http import HttpResponseRedirect


@login_required
def like_photo(request, photo_id):
   photo = get_object_or_404(Photo, id=photo_id)
   user = request.user
   
   if user in photo.likes.all():
       photo.likes.remove(user)
   else:
       photo.likes.add(user)
       
   return redirect("home")



@login_required
def add_comment(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    
    if request.method == "POST":
        content = request.POST.get("comment")
        
        comment = Comment(photo=photo, user=request.user, content=content)
        
        comment.save()
        
    return redirect("home")



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
