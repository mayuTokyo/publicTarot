from django import forms
from.models import Card
from django.contrib.auth.models import User


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

class ComentForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=['content']
        labels = {
        "content": "占い内容"
        }


class MainForm(forms.Form):
    class Meta:
        model=Card
        content=forms.CharField(label="占い内容",max_length=500, widget=forms.Textarea(attrs={'class':'from-control','rows':2,"placeholder":"占い内容"})) 


class ContactForm(forms.Form):
    subject = forms.CharField(
        label="件名",
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "件名",
            }
        )
    )
    email = forms.EmailField(
        label="メールアドレス",
            widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "メール"
            }
        )
    )
    message = forms.CharField(
        label="問い合わせ内容",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "問い合わせ内容"
            }
        )
    )

    def send_email(self, login_use):
        subject = "【お問い合わせ" + self.cleaned_data["subject"]
        message = self.cleaned_data["message"] + f"\n\nBy {login_use}."
        email = self.cleaned_data["email"]
        recipient_list = ["mayuiphoneau@gmail.com"] 
        try:
            send_mail(subject, message, email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")