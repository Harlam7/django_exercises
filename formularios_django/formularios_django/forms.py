from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escriba el nombre ome", max_length=100, help_text="100 max")
    url = forms.URLField(label="Tu sitio web", required=False, initial="http://")
    comment = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(label="Escriba el nombre ome:", max_length=50, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label="Tu sitio web", max_length=50)
    comment = forms.CharField(label="Mensaje")

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != "Open":
            raise forms.ValidationError("Tan solo el valor open está permitido en este campo")
        else:
            return name