from flask_table import Table, Col

class Results(Table):
    Id = Col('Id', show=False)
    Name = Col('Name')
    Descr = Col('Descr')
    Location = Col('Location')
