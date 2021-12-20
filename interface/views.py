from django.shortcuts import render


# Create your views here.
def index(request):
    context = { 
        "result": [12, 3, 7]
    }
    return render(request, "interface/index.html", context)


def contacts(request):
    return render(request, "interface/contacts.html", {})

def basket(request):
    return render(request, "interface/basket.html", {})