from flask import Flask, render_template, redirect, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

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
    pets = Pet.get_pets()
    
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    
    if form.validate_on_submit():
        return redirect('/')
    else:
        return render_template('add_pet.html')
    
    
    
    