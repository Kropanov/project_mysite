from django.shortcuts import render


# Create your views here.
def index(request):
    context = { 
        "result": [12, 3, 7]
    }
    return render(request, "interface/index.html", context)
