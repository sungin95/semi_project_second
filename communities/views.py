from django.shortcuts import render, redirect, get_object_or_404
from .form import ArticleForm, CommentForm, ArticleImageForm, NotionForm
from .models import Articles, Comments, ArticlesImages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Articles, Search
from django.core.paginator import Paginator
from datetime import date, datetime, timedelta
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def index(request):
    k = Articles.objects.exclude(category="공지").order_by("-id")
    bests = Articles.objects.exclude(category="공지").order_by("-like")[:10]
    notions = Articles.objects.filter(category="공지")
    print(bests)
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 20)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
        "bests": bests,
        "notions": notions,
        "category": "전체",
    }
    return render(request, "communities/index.html", context)


def index_jab(request):
    k = Articles.objects.filter(category="잡담").order_by("-id")
    bests = Articles.objects.exclude(category="공지").order_by("-like")[:10]
    notions = Articles.objects.filter(category="공지")
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 20)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
        "bests": bests,
        "notions": notions,
        "category": "잡담",
    }
    return render(request, "communities/index.html", context)


def index_question(request):
    k = Articles.objects.filter(category="질문").order_by("-id")
    bests = Articles.objects.exclude(category="공지").order_by("-like")[:10]
    notions = Articles.objects.filter(category="공지")
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 20)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
        "bests": bests,
        "notions": notions,
        "category": "질문",
    }
    return render(request, "communities/index.html", context)


def index_boast(request):
    k = Articles.objects.filter(category="자랑").order_by("-id")
    bests = Articles.objects.exclude(category="공지").order_by("-like")[:10]
    notions = Articles.objects.filter(category="공지")
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 20)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
        "bests": bests,
        "notions": notions,
        "category": "자랑",
    }
    return render(request, "communities/index.html", context)


def index_consult(request):
    k = Articles.objects.filter(category="고민/상담").order_by("-id")
    bests = Articles.objects.exclude(category="공지").order_by("-like")[:10]
    notions = Articles.objects.filter(category="공지")
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 20)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
        "bests": bests,
        "notions": notions,
        "category": "고민/상담",
    }
    return render(request, "communities/index.html", context)


def index_hello(request):
    k = Articles.objects.filter(category="인사").order_by("-id")
    bests = Articles.objects.exclude(category="공지").order_by("-like")[:10]
    notions = Articles.objects.filter(category="공지")
    page = request.GET.get("page", "1")
    paginator = Paginator(k, 20)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
        "bests": bests,
        "notions": notions,
        "category": "인사",
    }
    return render(request, "communities/index.html", context)


@login_required
def article_create(request):
    ImageFormSet = modelformset_factory(ArticlesImages, form=ArticleImageForm, extra=3)
    user = request.user
    if request.method == "POST":
        articleForm = ArticleForm(request.POST)
        formset = ImageFormSet(
            request.POST, request.FILES, queryset=ArticlesImages.objects.none()
        )
        if articleForm.is_valid() and formset.is_valid():
            article_form = articleForm.save(commit=False)
            article_form.user = request.user
            article_form.save()
            user.point += 1000
            user.save()
            for forms in formset.cleaned_data:
                if forms:
                    image = forms["image"]
                    photo = ArticlesImages(articles=article_form, image=image)
                    photo.save()
            return redirect("communities:index")
        else:
            print(article_form.errors, formset.errors)
    else:
        articleForm = ArticleForm()
        formset = ImageFormSet(queryset=ArticlesImages.objects.none())
    context = {
        "articleForm": articleForm,
        "formset": formset,
    }
    return render(request, "communities/form.html", context)


@login_required
def update(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    ImageFormSet = modelformset_factory(ArticlesImages, form=ArticleImageForm, extra=3)
    if article.user == request.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            formset = ImageFormSet(
                request.POST,
                request.FILES,
                queryset=ArticlesImages.objects.none(),
            )
            if form.is_valid() and formset.is_valid():
                article_ = form.save(commit=False)
                article_.user = request.user
                article_.save()
                for forms in formset.cleaned_data:
                    if forms:
                        image = forms["image"]
                        photo = ArticlesImages(articles=article_, image=image)
                        photo.save()
                return redirect("communities:detail", article.pk)
            else:
                print(form.errors, formset.errors)
        else:
            form = ArticleForm(instance=article)
            formset = ImageFormSet(
                queryset=ArticlesImages.objects.none(),
            )
        context = {
            "article": article,
            "articleForm": form,
            "formset": formset,
        }
        return render(request, "communities/form.html", context)
    return redirect("communities:detail", article.pk)


def detail(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comments_set.all()

    article_content = article.content.split("\n")
    content = {
        "article_content": article_content,
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
    }
    response = render(request, "communities/detail.html", content)
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get("hitblog", "_")

    if f"_{article_pk}_" not in cookie_value:
        cookie_value += f"{article_pk}_"
        response.set_cookie(
            "hitblog", value=cookie_value, max_age=max_age, httponly=True
        )
        article.hits += 1
        article.save()

    return response


@login_required
def article_delete(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    if article.user == request.user:
        if request.method == "POST":
            article.delete()
            return redirect("communities:index")
    return redirect("communities:detail", article_pk)


@login_required
def comment_create(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.Articles = article
        comment.user = request.user
        user = request.user
        user.point += 100
        user.save()
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
        user = request.user
        user.point += 100
        user.save()
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


@login_required
def like(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    if article.like.filter(pk=request.user.pk).exists():
        article.like.remove(request.user)
        is_like = False
    else:
        article.like.add(request.user)
        is_like = True
    context = {
        "isLiked": is_like,
        "likeCount": article.like.count(),
    }
    return JsonResponse(context)


@login_required
def notion_create(request):
    ImageFormSet = modelformset_factory(ArticlesImages, form=ArticleImageForm, extra=3)
    if request.user.is_superuser:
        if request.method == "POST":
            articleForm = NotionForm(request.POST)
            formset = ImageFormSet(
                request.POST, request.FILES, queryset=ArticlesImages.objects.none()
            )
            if articleForm.is_valid() and formset.is_valid():
                article_form = articleForm.save(commit=False)
                article_form.category = "공지"
                article_form.user = request.user
                article_form.save()
                for forms in formset.cleaned_data:
                    if forms:
                        image = forms["image"]
                        photo = ArticlesImages(articles=article_form, image=image)
                        photo.save()
                return redirect("communities:index")
            else:
                print(article_form.errors, formset.errors)
        else:
            articleForm = NotionForm()
            formset = ImageFormSet(queryset=ArticlesImages.objects.none())
        context = {
            "articleForm": articleForm,
            "formset": formset,
        }
        return render(request, "communities/form.html", context)
    else:
        return redirect("communities:index")


@login_required
def notion_update(request, article_pk):
    article = get_object_or_404(Articles, pk=article_pk)
    ImageFormSet = modelformset_factory(ArticlesImages, form=ArticleImageForm, extra=3)
    if article.user == request.user:
        if request.method == "POST":
            form = NotionForm(request.POST, request.FILES, instance=article)
            formset = ImageFormSet(
                request.POST,
                request.FILES,
                queryset=ArticlesImages.objects.none(),
            )
            if form.is_valid() and formset.is_valid():
                article_ = form.save(commit=False)
                article_.user = request.user
                article_.save()
                for forms in formset.cleaned_data:
                    if forms:
                        image = forms["image"]
                        photo = ArticlesImages(restaurant=article, image=image)
                        photo.save()
                return redirect("communities:detail", article.pk)
            else:
                print(form.errors, formset.errors)
        else:
            form = NotionForm(instance=article)
            formset = ImageFormSet(
                queryset=ArticlesImages.objects.none(),
            )
        context = {
            "article": article,
            "articleForm": form,
            "formset": formset,
        }
        return render(request, "communities/form.html", context)
    return redirect("communities:detail", article.pk)


def search(request):
    if request.method == "GET":
        communities = Articles.objects.all()
        search = request.GET.get("search", "")

        if len(search) >= 1:
            if Search.objects.filter(keyword=search).exists():
                search_keyword = Search.objects.get(keyword=search)
                search_keyword.count += 1
                search_keyword.save()
            else:
                Search.objects.create(keyword=search, count=1)

        if search:
            search_list = communities.filter(
                Q(category__icontains=search)
                | Q(title__icontains=search)
                | Q(content__icontains=search)
                | Q(user__username__icontains=search)
            )
            context = {
                "search_list": search_list,
                "search": search,
            }
            return render(request, "communities/search.html", context)
