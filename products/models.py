from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    모델명 = models.TextField(blank=True, null=True)
    가격 = models.IntegerField(blank=True, null=True)
    썸네일 = models.TextField(blank=True, null=True)
    이미지1 = models.TextField(blank=True, null=True)
    이미지2 = models.TextField(blank=True, null=True)
    이미지3 = models.TextField(blank=True, null=True)
    제조회사 = models.TextField(blank=True, null=True)
    등록년월 = models.TextField(blank=True, null=True)
    운영체제 = models.TextField(blank=True, null=True)
    게임용 = models.BooleanField(blank=True, null=True)
    사무_인강용 = models.BooleanField(blank=True, null=True)
    그래픽작업용 = models.BooleanField(blank=True, null=True)
    화면크기 = models.TextField(blank=True, null=True)
    화면비율 = models.TextField(blank=True, null=True)
    해상도 = models.TextField(blank=True, null=True)
    화면크기대 = models.TextField(blank=True, null=True)
    DCI_P3 = models.IntegerField(blank=True, null=True)
    NTSC = models.TextField(blank=True, null=True)
    AdobeRGB = models.TextField(blank=True, null=True)
    QLED = models.BooleanField(blank=True, null=True)
    화면밝기 = models.IntegerField(blank=True, null=True)
    주사율 = models.TextField(blank=True, null=True)
    패널종류 = models.TextField(blank=True, null=True)
    패널표면처리 = models.TextField(blank=True, null=True)
    CPU제조사 = models.TextField(blank=True, null=True)
    CPU종류 = models.TextField(blank=True, null=True)
    CPU코드명 = models.TextField(blank=True, null=True)
    CPU넘버 = models.TextField(blank=True, null=True)
    코어수 = models.TextField(blank=True, null=True)
    스레드수 = models.IntegerField(blank=True, null=True)
    메모리타입 = models.TextField(blank=True, null=True)
    메모리용량 = models.IntegerField(blank=True, null=True)
    메모리슬롯 = models.TextField(blank=True, null=True)
    메모리최대용량 = models.IntegerField(blank=True, null=True)
    메모리대역폭 = models.IntegerField(blank=True, null=True)
    메모리교체 = models.TextField(blank=True, null=True)
    메모리구성 = models.TextField(blank=True, null=True)
    저장장치종류 = models.TextField(blank=True, null=True)
    저장용량 = models.IntegerField(blank=True, null=True, default=0)
    저장슬롯 = models.TextField(blank=True, null=True)
    GPU종류 = models.TextField(blank=True, null=True)
    GPU제조사 = models.TextField(blank=True, null=True)
    GPU칩셋 = models.TextField(blank=True, null=True)
    TGP = models.IntegerField(blank=True, null=True)
    GPU기술 = models.TextField(blank=True, null=True)
    GPU메모리 = models.IntegerField(blank=True, null=True)
    게임관련기능 = models.TextField(blank=True, null=True)
    무선랜 = models.TextField(blank=True, null=True)
    유선랜 = models.TextField(blank=True, null=True)
    블루투스 = models.TextField(blank=True, null=True)
    HDMI = models.FloatField(blank=True, null=True)
    MicroHDMI = models.BooleanField(blank=True, null=True)
    USB = models.TextField(blank=True, null=True)
    USB_PD = models.BooleanField(blank=True, null=True)
    썬더볼트3 = models.TextField(blank=True, null=True)
    썬더볼트4 = models.TextField(blank=True, null=True)
    USB_C = models.IntegerField(blank=True, null=True)
    USB_A = models.IntegerField(blank=True, null=True)
    RGB라이트 = models.IntegerField(blank=True, null=True)
    숫자키패드 = models.BooleanField(blank=True, null=True)
    배터리 = models.TextField(blank=True, null=True)
    어댑터 = models.TextField(blank=True, null=True)
    충전단자 = models.TextField(blank=True, null=True)
    두께 = models.TextField(blank=True, null=True)
    무게 = models.TextField(blank=True, null=True)
    적합성평가인증 = models.TextField(blank=True, null=True)
    안전확인인증 = models.TextField(blank=True, null=True)
    D_SUB = models.BooleanField(blank=True, null=True)
    HDD = models.IntegerField(blank=True, null=True)
    MicroSD카드 = models.BooleanField(blank=True, null=True)
    ODD종류 = models.TextField(blank=True, null=True)
    PANTONE = models.BooleanField(blank=True, null=True)
    SD카드 = models.BooleanField(blank=True, null=True)
    TPM = models.BooleanField(blank=True, null=True)
    UFS = models.BooleanField(blank=True, null=True)
    miniDP = models.BooleanField(blank=True, null=True)
    miniLED = models.BooleanField(blank=True, null=True)
    sRGB = models.TextField(blank=True, null=True)
    게임관련기능 = models.TextField(blank=True, null=True)
    고속충전 = models.BooleanField(blank=True, null=True)
    광시야각 = models.BooleanField(blank=True, null=True)
    돌비비전 = models.BooleanField(blank=True, null=True)
    멀티리더기 = models.BooleanField(blank=True, null=True)
    상품구분 = models.TextField(blank=True, null=True)
    셀룰러 = models.TextField(blank=True, null=True)
    슬림형베젤 = models.BooleanField(blank=True, null=True)
    얼굴인식 = models.BooleanField(blank=True, null=True)
    웹캠 = models.BooleanField(blank=True, null=True)
    웹캠OFF지원 = models.BooleanField(blank=True, null=True)
    제품분류 = models.TextField(blank=True, null=True)
    지문인식 = models.BooleanField(blank=True, null=True)
    쿨링팬 = models.TextField(blank=True, null=True)
    키보드라이트 = models.BooleanField(blank=True, null=True)
    침수지연키보드 = models.BooleanField(blank=True, null=True)
    터치스크린 = models.BooleanField(blank=True, null=True)
    트루톤 = models.BooleanField(blank=True, null=True)
    화면회전각 = models.TextField(blank=True, null=True)
    휴대용 = models.BooleanField(blank=True, null=True)
    전용펜지원 = models.BooleanField(blank=True, null=True)
    DPAltMode = models.BooleanField(blank=True, null=True)
    리프트힌지 = models.BooleanField(blank=True, null=True)
    CPU제조사분류 = models.TextField(blank=True, null=True)
    CPU넘버분류 = models.TextField(blank=True, null=True)
    표준텐키리스 = models.BooleanField(blank=True, null=True)
    와이드뷰 = models.BooleanField(blank=True, null=True)
    AppleT2 = models.BooleanField(blank=True, null=True)
    기계식키보드 = models.BooleanField(blank=True, null=True)
    like_product = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_user"
    )
    ten_price = models.IntegerField(blank=True, null=True)
    가격등급 = models.TextField(blank=True, null=True)
    저장용량등급 = models.TextField(blank=True, null=True)
    GPU종류등급 = models.TextField(blank=True, null=True)
    해상도등급 = models.TextField(blank=True, null=True)
    화면크기등급 = models.TextField(blank=True, null=True)
    무게등급 = models.TextField(blank=True, null=True)


class Review(models.Model):
    products = models.ForeignKey("Products", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    grade = models.FloatField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(0)]
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

    # purchase = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name="purchased_users"
    # )


class Purchase(models.Model):
    products = models.ForeignKey("Products", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    content = models.TextField(blank=True, null=True)  # 배송 메시지
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
