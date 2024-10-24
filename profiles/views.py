from django.shortcuts import render, redirect

from profiles.models import Profile


def detailed_profile(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile
    }
    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    return render(request, 'profiles/profile-delete.html')

