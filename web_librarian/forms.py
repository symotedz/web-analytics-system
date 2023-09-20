import datetime
from django.forms import ModelForm
from . models import *


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        
class BookRenderForm(ModelForm):
    class Meta:
        model = Books_render
        fields = '__all__'
        