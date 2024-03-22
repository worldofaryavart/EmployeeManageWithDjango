from django import forms
from .models import Personal, Office, Salary

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'gender', 'city', 'birthdate', 'phone']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['ecode', 'name', 'post', 'joining', 'basicpay']
        widgets = {
            'joining': forms.DateInput(attrs={'type': 'date'}),
        }

# from django import forms
# from .models import Personal, Office, Salary

# forms.py
class SalaryForm(forms.ModelForm):
    ecode = forms.CharField(label='Employee Code')

    class Meta:
        model = Salary
        fields = ['ecode', 'months', 'overtime']

    def save(self, commit=True):
        instance = super().save(commit=False)
        ecode = self.cleaned_data.get('ecode')
        months = self.cleaned_data.get('months')
        overtime = self.cleaned_data.get('overtime')

        try:
            office = Office.objects.get(ecode=ecode)
        except Office.DoesNotExist:
            raise forms.ValidationError('Invalid employee code.')

        total_days = months * 30 + overtime
        final_pay = office.basicpay * (total_days / 30)

        # Round the final pay to the nearest whole number
        final_pay = round(final_pay)

        instance.finalpay = final_pay

        if commit:
            instance.save()
        return instance
