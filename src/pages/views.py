from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<button>Hello Vibhu World</button>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})
