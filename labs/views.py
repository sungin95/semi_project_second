from django.shortcuts import render
from dotenv import load_dotenv
import os

# Create your views here.
def main(request):
    context = {}
    return render(request, "labs/main.html", context)

def rating(request):
    return render(request, "labs/rating.html")

def intro(request):
    load_dotenv()
    MAPKEY = os.getenv("MAPKEY")
    context = {
        'MAPKEY': MAPKEY,
    }
    return render(request, "labs/intro.html", context)