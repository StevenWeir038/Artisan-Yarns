from django.shortcuts import render


def newsletter(request):
    """ Newsletter page view """

    template = 'newsletter/newsletter.html'
    
    return render(request, template)