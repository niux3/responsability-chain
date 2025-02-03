import json
from random import randint
from faker import Faker
from flask import render_template, redirect, url_for, flash, request
from .app import app, db
from .models import User, Company
from .forms import UserForm, SearchForm, fields, filters, date_filter
from app.libs import Filters


@app.route('/')
def index():
    ctx = {
        'object_list': User.query.all()
    }
    return render_template('index.html', **ctx)

@app.route('/ajouter.html', methods=['GET', 'POST'], defaults={"id": 0})
@app.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    if id != 0:
        instance = User.query.get_or_404(id)
    form = UserForm(obj=instance if id != 0 else None)
    if form.validate_on_submit():
        if id == 0:
            instance = User(**{k:v for k, v in form.data.items() if k != 'csrf_token'})
        else:
            form.populate_obj(instance)
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        flash(f"Votre utilisateur a bien été {'édité' if id != 0 else 'ajouté'}", "success")
        return redirect(url_for('index'))
    ctx = {
        'form': form
    }
    return render_template('edit.html', **ctx)

@app.route('/ajouter-utilisateurs.html')
def import_user():
    fake = Faker('fr_fr')
    for _ in range(50):
        data = {
            'name': fake.company()
        }
        company = Company(**data)
        db.session.add(company)
        db.session.commit()
        db.session.refresh(company)
    for _ in range(300):
        profile = fake.profile()
        data = {
            "name": fake.name(),
            "username": profile.get('username'),
            "birthday": profile.get('birthdate'),
            "email": fake.email(),
            "website": profile.get('website').pop(),
            "ssn": profile.get('ssn'),
            "sex": profile.get('sex'),
            "phone": fake.phone_number(),
            "address_city": fake.city(),
            "address_street": fake.street_address(),
            "address_zipcode": fake.postcode(),
            "address_lat": fake.latitude(),
            "address_long": fake.longitude(),
            "company_id": randint(1, 50),
        }
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
    return redirect(url_for('index'))

@app.route('/<int:id>-supprimer.html')
def destroy(id):
    instance = User.query.get_or_404(id)
    db.session.delete(instance)
    db.session.commit()
    flash("Votre utilisateur a bien été supprimé", "success")
    return redirect(url_for('index'))

@app.route('/chercher.html', methods=['GET'])
def search():
    form = SearchForm()
    if request.args.get('submit') is not None:
        query = User.query
        
        filter_conditions = Filters.build_conditions(request.args)
        query = Filters.execute(query, filter_conditions)
        # from sqlalchemy import or_
        # query = query.filter(or_(User.username == 'ACOLLET', User.username == 'acollet'))
        ctx = {
            'object_list': query.all() 
        }
        return render_template('index.html', **ctx)
    ctx = {
        'form': form,
        'fields': json.dumps(fields),
        'comparator': {
            'normal': json.dumps(filters),
            'date': json.dumps(date_filter)
        }

    }
    return render_template('search.html', **ctx)
