import wtforms
from wtforms_alchemy import ModelForm
from flask_wtf import FlaskForm
from .models import User

filters = [
    "Choisir un filtre",
    "Est égal à",
    "N'est pas égal à",
    "Est égal à (Ne respecte pas la casse)",
    "N'est pas égal à (Ne respecte pas la casse)",
    "Contient",
    "Ne contient pas",
    "Contient (Ne respecte pas la casse)",
    "Ne contient pas (Ne respecte pas la casse)",
    "Commence par",
    "Ne commence pas par",
    "Commence par (Ne respecte pas la casse)",
    "Ne commence pas par (Ne respecte pas la casse)",
    "Se termine par",
    "Ne se termine pas par",
    "Se termine par (Ne respecte pas la casse)",
    "Ne se termine pas par (Ne respecte pas la casse)",
    "Est vide",
]

fields_users = { 
    "nom": "name",
    "pseudo": "username",
    "email": "email",
    "site web": "website",
    "ssn": "ssn",
    "sex": "sex",
    "téléphone": "phone",
    "ville": "address_city",
    "rue": "address_street",
    "code postal": "address_zipcode",
    "latitude": "address_lat",
    "longitude": "address_long",
    # "": "company",
    "date anniversaire": "birthday",
    "date création": "created",
    "date mise à jour": "updated",
}
fields_company = {
    "nom": "name",
    "date création": "created",
    "date mise à jour": "updated",
}

date_filter = [
    "choisir un type de comparateur de date",
    "Personnalisé",
    "Année précédente",
    "Année courante",
    "Année suivante",
    "Trimestre précédent",
    "Trimestre courant",
    "Trimestre suivant",
    "Mois précédent",
    "Mois courant",
    "Mois suivant",
    "Hier",
    "Aujourd'hui",
    "Demain",
    "Dans le futur",
    "Dans le passé",
]

type_filter = [
    "Toutes les conditions sont remplies", 
    "Au moins une condition est remplie"
]

class UserForm(FlaskForm, ModelForm):
    class Meta:
        model = User

data_field_0 = {                                                                                                                
    'société': [(f'company_{i}', f'{r} (société)') for i, r in enumerate(fields_company.keys())],                                                                                   
    'employé': [(f'user_{i}', f'{r} (employé)') for i, r in enumerate(fields_users.keys())],                                                                                   
}

class SearchForm(FlaskForm):
    name = wtforms.StringField("Nom", validators=[wtforms.validators.DataRequired()])
    accepted = wtforms.RadioField("La fiche est acceptée si", choices=[(i, r) for i, r in enumerate(type_filter, 1)])
    field_0 = wtforms.SelectField("Champs", choices=data_field_0)
    field_filter_0 = wtforms.SelectField("Filtres", choices=[(i, r) for i, r in enumerate(filters)])
    field_value_0 = wtforms.StringField("Valeur")
    # date_0 = wtforms.SelectField("Date", choices=[(i, r) for i, r in enumerate(date_field)])
    # date_filter_0 = wtforms.SelectField("Filtre", choices=[(i, r) for i, r in enumerate(date_filter)])
    # date_begin_0 = wtforms.StringField("De")
    # date_end_0 = wtforms.StringField("À")
