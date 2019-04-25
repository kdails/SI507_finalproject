# forms.py
from wtforms import Form, StringField, SelectField

class ParkSearchForm(Form):
    choices = [('Name', 'Name'),
               ('Descr', 'Descr'),
               ('Location', 'Location')]
    select = SelectField('See database columns :', choices=choices)
    search = StringField('')
