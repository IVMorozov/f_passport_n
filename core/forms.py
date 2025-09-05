from django import forms
from .models import  Review, ReviewAnswer
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm, 
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,

)
user_model = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta:
        model = user_model
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if user_model.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")
        return email

class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Имя пользователя"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль"}
        )

class ReviewModelForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["MO", "service", "text", "rating"]
        widgets = {
            "MO": forms.Select(attrs={"class": "form-control"}),
            "service": forms.Select(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-control"}),
        }

class ReviewAnswerModelForm(forms.ModelForm):

    class Meta:
        model = ReviewAnswer
        fields = ["answer_text", ]
        widgets = {
                "answer_text": forms.Textarea(attrs={"class": "form-control"}),
        }
