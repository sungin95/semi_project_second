from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Articles

# Create your views here.
def index(request):
    return render(request, "communities/index.html")


def detail(request):
    return render(request, "communities/detail.html")


@login_required
def comments(request, review_pk):
    article = Articles.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if request.method == "POST":
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
    context = {
        "comment": comment,
    }
    return redirect("communities:detail")
