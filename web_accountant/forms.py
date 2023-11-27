from django.forms import ModelForm

from web_super_admin.models import CashOut

class CashOutForm(ModelForm):
    class Meta:
        model = CashOut
        fields = "__all__"