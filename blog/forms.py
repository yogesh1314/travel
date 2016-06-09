from django import forms
from django.forms import ModelForm
from base.models import *
from multiupload.fields import MultiFileField

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['created_on', 'is_visible']  # not attachments!
        widgets = {
            'description': forms.Textarea(attrs={'class': 'input-field'})
        }
    images = MultiFileField(min_num=0, max_num=10, max_file_size=1024*1024*5)
    def __init__(self, *args, **kwargs):
        super(AddBlogForm, self).__init__(*args, **kwargs)
        self.fields['description'].required=True
        self.fields['title'].required=True
        self.fields['images'].required=False
    def save(self, commit=True):
        instance = super(AddBlogForm, self).save(commit=False)
        instance.save(commit)
        for each in self.cleaned_data['images']:
            ReviewImages.objects.create(image=each, review=instance)
        return instance