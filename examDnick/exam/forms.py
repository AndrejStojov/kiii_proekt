from django import forms
from exam.models import Exam
class ExamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Exam
        exclude= ('user',)
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'semester': forms.Select(attrs={'class': 'form-select'})
        }
