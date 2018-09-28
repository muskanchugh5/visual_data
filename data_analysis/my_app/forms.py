from django import forms
from my_app.models import plot_information

class Plotform(forms.ModelForm):
    class Meta():
        model=plot_information
        fields=('type_of_graph','title','no_of_var','x_col','y_col','data_file')


