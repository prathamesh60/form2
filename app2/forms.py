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

class MainDeptForm(forms.ModelForm):
    class Meta:
        model = MainDept
        fields = "__all__"

class MainDesignation(forms.ModelForm):
    class Meta:
        model = MainDesignation
        fields = "__all__"

class Staff(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class Scale(forms.ModelForm):
    class Meta:
        model = Scale
        fields = "__all__"
