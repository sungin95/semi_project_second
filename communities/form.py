from django import forms
from .models import Articles, Comments, ArticlesImages
from django.utils.translation import gettext_lazy as _


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            "title",
            "category",
            "content",
        ]


class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticlesImages
        fields = ("image",)
        labels = {
            "image": _("Image"),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            "content",
        ]


class NotionForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            "title",
            "content",
        ]
