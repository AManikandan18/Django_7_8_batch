from django.http import HttpResponse
import time

class Mymiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Middleware initialized...")
        
    def __call__(self,request):
        print("Before View (Request intercepted)")
        response = self.get_response(request)
        print("After View (Response going to browser)")
        return response

        