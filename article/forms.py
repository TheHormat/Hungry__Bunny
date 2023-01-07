from django import forms
from .models import Article,SendMailMessage



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class SendMailMessageForm(forms.ModelForm):
    class Meta:
        model = SendMailMessage
        fields = '__all__'     
        labels = {
            'name':"User Name",
            'mail_address':"Email Address",
            'messages':"Message"
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mail_address':forms.EmailInput(attrs={'class':'form-control'}),
            'messages':forms.Textarea(attrs={'class':'form-control'})

        }