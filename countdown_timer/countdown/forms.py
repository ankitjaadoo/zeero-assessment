from django import forms

class TimerForm(forms.Form):
    hours = forms.IntegerField(min_value=0, max_value=23, required=False, initial=0)
    minutes = forms.IntegerField(min_value=0, max_value=59, initial=0)
    seconds = forms.IntegerField(min_value=0, max_value=59, initial=0)

    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get('hours', 0)
        minutes = cleaned_data.get('minutes', 0)
        seconds = cleaned_data.get('seconds', 0)

        if hours == minutes == seconds == 0:
            raise forms.ValidationError("At least one value should be greater than zero.")
        return cleaned_data