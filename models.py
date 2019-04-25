from db import db

class State(db.Model):
    __tablename__ = 'States'
    Id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    Abbr = db.Column(db.String(2))
    State = db.Column(db.String(24))
    URL = db.Column(db.String(250))

    Parks_Rel = db.relationship('Park', secondary='association', back_populates='State_Rel', lazy='dynamic')

    def __init__(self, Abbr = None, State = None, URL = None, state_dict = None):
        self.Abbr = Abbr
        self.State = State
        self.URL = URL
        if state_dict:  # rewrite __init__() to accept raw dict as input for constructor
            self.Abbr = state_dict['Abbr']
            self.State = state_dict['State']
            self.URL = state_dict['URL']

    def __repr__(self):  # rewrite __repr__() to show user-friendly info
        return "{state_abbr} is the abbreviation for {state_state}. Copy and Paste, {own_URL} into your browser for more info".format(
            state_abbr = self.Abbr,
            state_state = self.State,
            own_URL = self.URL,
            )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Park(db.Model):
    __tablename__ = 'Parks'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(250))
    Descr = db.Column(db.String(2000))
    Location = db.Column(db.String(250))
    Type = db.Column(db.String(250))

    State_Rel = db.relationship('State',secondary='association',back_populates='Parks_Rel',lazy='dynamic')

    def __init__(self, Name = None, Descr = None, Type = None, Location = None, park_dict = None):
        self.Name = Name
        self.Descr = Descr
        self.Location = Location
        self.Type = Type
        if park_dict:  # rewrite __init__() to accept raw dict as input for constructor
            self.Name = park_dict['Name']
            self.Descr = park_dict['Descr']
            self.Location = park_dict['Location']
            self.Type = park_dict['Type']

    def __repr__(self):  # rewrite __repr__() to show user-friendly info
        return "{park_name}, a {park_type} in {location_name} : {park_descr}".format(
            park_name = self.Name,
            park_type = self.Type,
            location_name = self.Location,
            park_descr = self.Descr,
            )
              # use artist relationship here

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class StateParkAssociation(db.Model):
    __tablename__ = 'association'
    State_Id = db.Column(db.Integer, db.ForeignKey('States.Id'),primary_key=True)
    Park_Id = db.Column(db.Integer, db.ForeignKey('Parks.Id'),primary_key=True)
    State_Assoc = db.relationship("State", backref='Parks_Assoc')
    Park_Assoc = db.relationship("Park", backref='State_Assoc')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

# define table class
    # def __init__( self, Abbr= None, State= None, URL=None, state_dict =None):
    #     self.Abbr = Abbr
    #     self.State = State
    #     self.URL = URL
    #     if state_dict:
    #         self.Abbr = state_dict['']
