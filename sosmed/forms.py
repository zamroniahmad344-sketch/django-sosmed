from django import forms
from .models import Instagram

class InstagramForm(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = ['nama_depan', 'nama_belakang', 'username']
        
    def __init__(self, *args, **kwargs):
        super(InstagramForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})