from django import forms
from captcha.fields import CaptchaField

class SuggestionForm(forms.Form):
    title = forms.CharField(label="Название", max_length=384)
    link  = forms.URLField(label="Ссылка", max_length=512)
    text  = forms.CharField(label="Дополнительные детали", widget=forms.Textarea(), required=False)