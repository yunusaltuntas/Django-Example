from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(widget=forms.HiddenInput,required=False)
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data["botcatcher"]
        if len(botcatcher) >0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
