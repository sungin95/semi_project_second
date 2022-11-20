from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.utils import timezone
from django.template.defaultfilters import slugify


category_CHOICES = (
    ("잡담", "잡담"),
    ("질문", "질문"),
    ("자랑", "자랑"),
    ("고민/상담", "고민/상담"),
    ("인사", "인사"),
)


class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )
    category = models.CharField(max_length=50, choices=category_CHOICES)
    hits = models.PositiveIntegerField(default=0, verbose_name="조회수")
    #
    # object 를 Post 의 title 문자열로 반환
    def __str__(self):
        return self.title

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False


def get_image_filename(instance, filename):
    # 해당 Post 모델의 title 을 가져옴
    title = instance.articles.title
    # slug - 의미있는 url 사용을 위한 필드.
    # slugfy 를 사용해서 title을 slug 시켜줌.
    slug = slugify(title)
    # 제목 - 슬러그된 파일이름 형태
    return "post_images/%s-%s" % (slug, filename)


# default, upload_to 먼지 보기
class ArticlesImages(models.Model):
    # default = None 으로 이미지를 등록하지 않을 때는 db에 저장되지 않음.
    articles = models.ForeignKey(
        Articles, default=None, on_delete=models.CASCADE, related_name="articles_image"
    )
    # get_image_filename method 경로 사용
    # 문자열로 경로를 지정할 경우, media/문자열 지정 경로로 저장되며, 중간 디렉토리 경로를 지정할 수 있고,
    # 메소드(함수)로 지정할 경우, 중간 디렉토리 경로명뿐만 아니라 파일명까지 지정 가능
    image = models.ImageField(upload_to=get_image_filename)
    # admin 에서 모델이름
    class Meta:
        # 단수
        verbose_name = "Image"
        # 복수
        verbose_name_plural = "Images"

    # 이것도 역시 post title 로 반환
    def __str__(self):
        return str(self.articles)


class Comments(models.Model):
    Articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_comments"
    )

    # object 를 Post 의 title 문자열로 반환
    def __str__(self):
        return self.title

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False

class Search(models.Model):
    keyword = models.TextField(max_length=30)
    count = models.IntegerField(default=0)