from django.shortcuts import render


def profile(request):
    """ User's profile page view """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
