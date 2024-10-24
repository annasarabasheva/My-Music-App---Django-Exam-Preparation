from django.shortcuts import render, redirect

from albums.models import Album
from profiles.models import Profile
from profiles.forms import ProfileCreateForm


def home(request):
    profile = Profile.objects.first()

    if not profile:
        profile_form = ProfileCreateForm(request.POST or None)

        if request.method == 'POST':
            if profile_form.is_valid():
                profile_form.save()
                return redirect('home')

        context = {
            'form': profile_form,
            'profile': profile
        }
        return render(request, 'profiles/home-no-profile.html', context)

    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
        'profile': profile,
    }
    return render(request, 'profiles/home-with-profile.html', context)





