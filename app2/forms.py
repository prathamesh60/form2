from django import forms
from app2.models import *

class ReligionForm(forms.ModelForm):
    class Meta:
        model = Religion
        fields = "__all__"

class CasteForm(forms.ModelForm):
    class Meta:
        model = Caste
        fields = "__all__"

class SuplHeadForm(forms.ModelForm):
    class Meta:
        model = SuplHead
        fields = "__all__"

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = "__all__"

class DesignatureForm(forms.ModelForm):
    class Meta:
        model = Designature
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class TypeTranForm(forms.ModelForm):
    class Meta:
        model = TypeTran
        fields = "__all__"
