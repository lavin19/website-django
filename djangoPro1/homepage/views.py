from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hello, I am Lavin. Welcome to my page! 🎉")