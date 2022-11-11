from django.shortcuts import render

# Create your views here.
def main(request):
    context = {}
    return render(request, "labs/main.html", context)


def rating(request):
    return render(request, "labs/rating.html")
