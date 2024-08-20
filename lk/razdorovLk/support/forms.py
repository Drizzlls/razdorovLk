from django.forms import ModelForm, Textarea
from .models import Support

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = ['text', 'topic']
        widgets = {'text': Textarea(attrs={'class': 'input'}),}