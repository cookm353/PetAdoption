from flask import Flask, render_template, redirect, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'good boy'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_pets():
    """Home Page"""
    pets = Pet.get_pets()
    
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Form for adding pets"""
    form = AddPetForm()
    
    species = [(p.species, p.species.title()) for p in Pet.get_pets()]
    form.species.choices = species
    
    if form.validate_on_submit():
        pet_details = {'name': form.name.data, 'species': form.species.data,
                       'isAvailable': form.available.data}
        
        if form.photo_url.data:
            pet_details['photo_url'] = form.photo_url.data
        if form.age.data:
            pet_details['age'] = form.age.data
        if form.notes.data:
            pet_details['notes'] = form.notes.data
        
        Pet.add_pet(pet_details)
        
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/<pet_id>', methods=['GET', 'POST'])
def show_pet_details_and_edit_form(pet_id):
    """Pet detail page"""
    form = EditPetForm()
    pet = Pet.get_pet(pet_id)
    
    if form.validate_on_submit():
        return redirect(f'/{pet_id}', pet=pet, form=form)
    else:
        return render_template('edit_pet.html', form=form, pet=pet)