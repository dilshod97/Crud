from django import forms
from .models import News


class NewsCreate(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'