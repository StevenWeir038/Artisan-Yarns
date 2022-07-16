from django.shortcuts import render


def contact(request):
    """ Contact page view """

    # PLAN OF ATTACK

    # 1st check the request method

    # create a form instance

    # clean the data

    # if form is valid send the email
    
    # relay a success message to the user

    # if for is not valid create relay a failure message to the user

    # create a blank instance and allow user to repopulate

    # apass the form to the template via the context dictionary

    return render(request, 'contact/contact.html')
