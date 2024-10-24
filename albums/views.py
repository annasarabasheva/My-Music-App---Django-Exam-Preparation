from django.shortcuts import render, redirect

from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album
from profiles.models import Profile


def add_album(request):
    profile = Profile.objects.first()
    form = AlbumCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = profile
            album.save()
            return redirect('home')
    context = {
        "form": form,
    }
    return render(request, 'albums/album-add.html', context)


def detailed_album(request, id):
    album = Album.objects.get(id=id)

    context = {
        "album": album,
    }

    return render(request, 'albums/album-details.html', context)


def edit_album(request, id):
    album = Album.objects.get(id=id)
    form = AlbumEditForm(request.POST or None, instance=album)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form": form,
        "album": album

    }

    return render(request, 'albums/album-edit.html', context)


def delete_album(request, id):
    album = Album.objects.get(id=id)
    form = AlbumDeleteForm(instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('home')

    context = {
        "form": form,
        "album": album
    }

    return render(request, 'albums/album-delete.html', context)


