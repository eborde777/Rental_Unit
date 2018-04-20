from django import forms
from django.contrib.admin import widgets
from dal import autocomplete
from .models import Post, City, State


# THIS IS NEWER VERSION USING AUTOCOMPLETE LIGHT PAKAGE TO IMPLEMENT AJAX 
# follow http://django-autocomplete-light.readthedocs.io/en/master/tutorial.html

class PostForm(forms.ModelForm):
    # st = forms.ModelChoiceField(
    #     queryset = State.objects.all(),
    #     empty_label=None,
    #     widget=autocomplete.ModelSelect2(url='posts:state-autocomplete')
    # )
    available_from = forms.DateField(widget=forms.SelectDateWidget())
    
    class Meta:
        model = Post
        fields = [
            'rental_type',
            'title',
            'address',
            'address2',
            'state', 
            'cities',
            'zip_code' ,
            'available_from', 
            'accomodates', 
            'expected_rent' ,
            'posted_by', 
            'description' ,
        ]
        widgets = {
            'state': autocomplete.ModelSelect2(url='posts:state-autocomplete', attrs={'data-placeholder': 'State',}),
            'cities': autocomplete.ModelSelect2(url = 'posts:city-autocomplete',
                                                 forward=['state'], 
                                                 attrs={'data-placeholder': 'Select state first ...',}),
            "expected_rent":forms.TextInput(attrs={'placeholder':'$ 0.00',}),
            "address2" : forms.TextInput(attrs={'placeholder':'Apartment, Studio or Floor',}),
        }




#BELOW IS THE OLD VERSION WE WERE USING

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             'title',
#             'description' ,
#             'new_state', 
#             'cities',
#             'zip_code' ,
#             'available_from', 
#             'accomodates', 
#             'expected_rent' ,
#             'posted_by', 
#         ]
        
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['cities'].queryset = City.objects.none()


#         if 'state' in self.data:
#             try:
#                 state_id = int(self.data.get('state'))
#                 self.fields['cities'].queryset = City.objects.filter(state_id=state_id).order_by('city')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['cities'].queryset = self.instance.country.city_set.order_by('city')
