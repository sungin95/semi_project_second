from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("email", "first_name", "last_name")


class CustomUserChargeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("point",)


class ProfileCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("image",)
        label = {
            "image": "프로필",
        }


class MyLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={"placeholder": "아이디", "maxlength": "16"}
        )
        self.fields["username"].label = False
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"placeholder": "비밀번호"}
        )
        self.fields["password"].label = False


class MySignupForm(CustomUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            # 아이디
            attrs={"placeholder": "아이디를 입력해주세요", "maxlength": "16"}
        )
        self.fields["username"].label = False
        # 이메일
        self.fields["email"].widget = forms.TextInput(
            attrs={"placeholder": "예:intellilaps@gmail.com"}
        )
        self.fields["email"].label = False
        # 비밀번호1
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"placeholder": "비밀번호를 입력해주세요"}
        )
        self.fields["password1"].label = False
        # 비밀번호2
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"placeholder": "비밀번호 확인"}
        )
        self.fields["password2"].label = False
