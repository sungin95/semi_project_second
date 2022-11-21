from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    ProfileCustomUserChangeForm,
    MyLoginForm,
    MySignupForm,
    CustomUserChargeForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


@login_required
def index(request):
    users = get_user_model().objects.all()  # 저장된 모든 User를 가져온다.
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        if (len(request.POST["username"])) <= 16:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect("labs:main")
    else:
        form = MySignupForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect("labs:main")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            user = form.get_user()
            user.point += 500
            user.save()
            return redirect(request.GET.get("next") or "labs:main")
    else:
        form = MyLoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:login")


@login_required
def detail_all(request, pk):
    user = get_user_model().objects.get(pk=pk)
    user.delete()
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필 정보가 성공적으로 변경되었습니다.")
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context=context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileCustomUserChangeForm(
            request.POST, request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, "프로필사진이 성공적으로 변경되었습니다.")
            return redirect("accounts:detail", request.user.pk)
    else:
        form = ProfileCustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/profile.html", context=context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "비밀번호 변경이 성공적으로 완료되었습니다.")
            messages.warning(request, "새로 로그인해주세요.")
            return redirect("accounts:login")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def follow(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect("accounts:profile", person.username)


@login_required
def charging(request):
    if request.method == "POST":
        form = CustomUserChargeForm(request.POST, instance=request.user)
        if form.is_valid():
            charge = form.save(commit=False)
            if charge.point <= 10000:
                charge.회원등급 = "i3"
            elif charge.point > 10000:
                charge.회원등급 = "i5"
            elif charge.point >= 100000:
                charge.회원등급 = "i7"
            charge.save()
            return redirect("accounts:charging")
    else:
        form = CustomUserChargeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/charging.html", context)
