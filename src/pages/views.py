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
    my_context = {
        "my_text":"this is about us",
        "my_num": 1234,
        "my_list":[12,23,556]
    }
    return render(request, "contact.html", my_context)
