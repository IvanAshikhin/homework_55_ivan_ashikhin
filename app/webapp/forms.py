from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    description = forms.CharField(max_length=500, required=True, label='Задача')
    details = forms.CharField(max_length=500, required=True, label='Описание', widget=widgets.Textarea)
    status_choices = (('NEW', 'New'), ('IN PROGRESS', 'In Progress'), ('DONE', 'Done'))
    status = forms.ChoiceField(required=True, label='Статус', choices=status_choices)
    done_date = forms.DateField(label='Дата выполнения', required=True,
                                widget=forms.NumberInput(attrs={'type': 'date'}))
