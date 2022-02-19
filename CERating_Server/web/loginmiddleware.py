from django.shortcuts import redirect
from django.urls import reverse
import re


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("hello")
        # One-time configuration and initialization.

    def __call__(self, request):
        # path = request.path
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # urllist = ['/enterprise_login/']
        # if not request.session.get('is_login',None) or not re.match(r'^/enterprise_login/',path):
        #     return redirect(reverse("enterprise_login/"))
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response