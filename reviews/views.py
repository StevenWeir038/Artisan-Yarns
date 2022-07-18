from django.shortcuts import render


def reviews(request):
    """ Reviews page view """

    template = 'reviews/reviews.html'

    return render(request, template)
