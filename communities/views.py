from django.shortcuts import render, redirect, get_object_or_404
from .form import ArticleForm, CommentForm
from .models import Articles, Comments
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Articles
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    k = Articles.objects.all().order_by("id")
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 3)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
    }
    return render(request, "communities/index.html", context)


@login_required
def article_create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("communities:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "communities/form.html", context)


def detail(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    comment_form = CommentForm()
    content = {
        "article": article,
        "comments": article.comments_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "communities/detail.html", content)


@login_required
def article_delete(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    if article.user == request.user:
        if request.method == "POST":
            article.delete()
            return redirect("communities:index")


@login_required
def update(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    if request.user == article.user:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect("communities:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {"article_form": article_form}
        return render(request, "communities/form.html", context)
    else:
        return redirect("communities:detail", article.pk)


@login_required
def comment_create(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.Articles = article
        comment.user = request.user
        comment.save()
        context = {
            "content": comment.content,
            "userName": comment.user.username,
        }
        return JsonResponse(context)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comments, pk=comment_pk)
    if request.user == comment.user:
        if request.method == "POST":
            comment.delete()
        return redirect("communities:detail", article_pk)
    return redirect("communities:detail", article_pk)


@login_required
def sub_comment_create(request, article_pk, comment_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    parent = Comments.objects.get(pk=comment_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.Articles = article
        comment.user = request.user
        comment.parent = parent
        comment.save()
        return redirect("communities:detail", article_pk)
    return redirect("communities:detail", article_pk)


@login_required
def sub_comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comments, pk=comment_pk)
    if request.user == comment.user:
        if request.method == "POST":
            comment.delete()
        return redirect("communities:detail", article_pk)
    return redirect("communities:detail", article_pk)
