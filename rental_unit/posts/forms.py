from django import forms
from .models import Post, City

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description' ,
            'new_state', 
            'citites',
            'zip_code' ,
            'available_from', 
            'accomodates', 
            'expected_rent' ,
            'posted_by', 
        ]
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        if 'state' not in self.data:
            self.fields['citites'].queryset = City.objects.none()

        else:
            if 'state' in self.data:
                try:
                    state_id = int(self.data.get('state'))
                    self.fields['citites'].queryset = City.objects.filter(state_id=state_id).order_by('city')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['citites'].queryset = self.instance.country.city_set.order_by('city')


