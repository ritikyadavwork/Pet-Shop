from allauth.account.adapter import get_adapter
from allauth.account.forms import SignupForm
from allauth.account.utils import setup_user_email
from allauth.account.models import EmailAddress
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from django import forms
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError

from classbasedview.ecom.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('title', css_class='col-md-6'),
                Div('product_name', css_class='col-md-6'),
                Div('price', css_class='col-md-6'),
                Div('stock', css_class='col-md-6'),
                Div('image', css_class='col-md-6'),
                Div('description', css_class='col-md-12'),
                css_class='row',
            ),
        )
        self.helper.form_tag = False
        self.helper.disable_csrf = True
