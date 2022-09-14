from django import forms
from django.core.exceptions import ValidationError
from .models import New


class Post:
    pass


class PostForm(forms.ModelForm):
    post_heading = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'post_heading',
            'post_text',
            'post_cat',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("post_heading")
        text = cleaned_data.get("post_text")

        if heading == text:
            raise ValidationError(
                "Заголовок не должно быть идентичен тексту статьи."
            )
        return cleaned_data