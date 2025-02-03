from datetime import datetime
from sqlalchemy.orm import relationship, backref
from .app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    website = db.Column(db.String)
    phone = db.Column(db.String)
    sex = db.Column(db.String)
    ssn = db.Column(db.String, unique=True)
    birthday = db.Column(db.Date, nullable=True)
    address_city = db.Column(db.String)
    address_street = db.Column(db.String)
    address_zipcode = db.Column(db.String)
    address_lat = db.Column(db.Numeric(10, 7))
    address_long = db.Column(db.Numeric(10, 7))
    company_id = db.Column(db.ForeignKey('companies.id', onupdate='CASCADE', ondelete='CASCADE'))
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        tpl = '<%s id="%s" email="%s" ssn="%s">'
        return tpl % (__class__.__name__, self.id, self.email, self.ssn)


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    users = relationship('User', backref=backref('companies'))

    def __repr__(self):
        tpl = '<%s id="%s" name="%s">'
        return tpl % (__class__.__name__, self.id, self.name)
