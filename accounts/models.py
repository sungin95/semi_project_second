from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class User(AbstractUser):
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    followings = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
    )
    point = models.IntegerField(default=1, blank=True, null=True)
    νμλ±κΈ = models.TextField(default="i3", blank=True, null=True)
