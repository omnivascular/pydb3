from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class DisplayForm(forms.Form):
    item_entry = forms.CharField(max_length=300, help_text="Enter item to search")
    quantity_changed = forms.IntegerField(help_text="enter quantity to update")

    def clean_item_entry(self):
        data = self.cleaned_data["item_entry"]
        return data

    def clean_quantity_change(self):
        data = self.cleaned_data["quantity_changed"]
        if data < 0:
            raise ValidationError(_("Invalid quantity, must be 0 or greater."))
        return data
