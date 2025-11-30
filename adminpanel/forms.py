from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=254,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'w-full px-3 py-2 rounded border focus:outline-none focus:ring-2 focus:ring-[#d3b689]',
            'placeholder': _('Username')
        })
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 rounded border focus:outline-none focus:ring-2 focus:ring-[#d3b689]',
            'placeholder': _('Password')
        })
    )


from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Slider

class SliderForm(forms.ModelForm):
    description_fr = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    description_en = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    description_ar = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Slider
        fields = [
            'image',
            'title_fr', 'title_en', 'title_ar',
            'description_fr', 'description_en', 'description_ar',
            'order', 'is_active'
        ]
