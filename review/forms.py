from django import forms
from .models import Review

# class reviewForm(forms.Form):
#     user_name=forms.CharField(label="user_name",error_messages={
#         "required":"user name should not be empty",
#         "max_length":"user name should be short"
#     })
#     rating=forms.IntegerField(label="Rating",min_value=1,max_value=5)
#     feedback=forms.CharField(label="Feedback",widget=forms.Textarea,max_length=200)


class reviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        labels={
            "user_name":"Your name",
            "feedback":"Your feedback",
            "rating":"Your Rating"
        }
        error_messages={
              "required":"user name should not be empty",
               "max_length":"user name should be short"
            
        }

