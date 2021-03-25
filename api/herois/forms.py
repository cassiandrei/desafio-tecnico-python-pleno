from django import forms

from herois.models import Heroi


class HeroiForm(forms.ModelForm):
    class Meta:
        model = Heroi
        exclude = '__all__'

    def __init__(self, *args, **kwargs):
        super(HeroiForm, self).__init__(*args, **kwargs)
        self.fields['foto'].required = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
