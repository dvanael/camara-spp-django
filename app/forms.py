from django import forms


class ESICForm(forms.Form):
    nome_completo = forms.CharField(
        max_length=255,
        label="NOME COMPLETO",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome', 'id': 'InputName'})
    )
    email = forms.EmailField(
        label="E-MAIL",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail', 'id': 'InputEmail', 'type': 'email'})
    )
    descricao = forms.CharField(
        label="DESCRIÇÃO A SUA SOLICITAÇÃO",
        required=True,
        widget=forms.Textarea(attrs={'id': 'InputDesc'})
    )


class OuvidoriaForm(forms.Form):
    nome = forms.CharField(
        max_length=255,
        label="NOME COMPLETO",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome', 'id': 'InputName'})
    )
    descricao = forms.CharField(
        label="DESCREVA SUA MANIFESTAÇÃO",
        required=True,
        widget=forms.Textarea(attrs={'id': 'InputDesc'})
    )


