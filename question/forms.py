from django import forms
import models


class QuestionForm(forms.ModelForm):
    email = forms.CharField()
    pregunta = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.Pregunta
        fields = ('email', 'pregunta',)
        exclude = ('state', 'respuesta')
    # end class


class QuestionFormAdmin(forms.ModelForm):
    pregunta = forms.CharField(widget=forms.Textarea)
    respuesta = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.Pregunta
        fields = ('email', 'pregunta', 'respuesta', 'state')
    # end class
