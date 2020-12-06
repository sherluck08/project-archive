from django import forms
from django.forms import ClearableFileInput
from .models import Archive


class ArchiveForm(forms.ModelForm):

    class Meta:
        model = Archive
        fields = ("title", "description")
        # widgets = {"project_file": ClearableFileInput(
        #     attrs={"multiple": True}), }
