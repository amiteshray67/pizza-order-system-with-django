from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1= forms.CharField(label='Topping 1', max_length=100)
#     topping2= forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
#     # cheese = forms.BooleanField(required=False)
#     # toppings = forms.MultipleChoiceField(choices=[('Pepperoni', 'Pepperoni'), ('Sausage', 'Sausage'), ('Onion', 'Onion'), ('Mushroom', 'Mushroom'), ('Pineapple', 'Pineapple')], widget=forms.CheckboxSelectMultiple)


class PizzaForm(forms.ModelForm):
    
    # size=forms.ModelChoiceField(queryset=Size.objects.all(), empty_label="Select a size")
    
    image= forms.ImageField(required=False)
    
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size'
        }
        # widgets = {
        #     'topping1': forms.TextInput(attrs={'placeholder': 'Topping 1'}),
        #     'size': forms.CheckboxSelectMultiple()
        # }
        
class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)        
