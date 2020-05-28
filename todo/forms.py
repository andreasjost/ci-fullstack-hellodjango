from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    # inner class: Tell the form which Model it's going to be associated with
    class Meta:
        model = Item
        fields = {'name', 'done'}
