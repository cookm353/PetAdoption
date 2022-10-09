from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.sql as sql

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True, 
            autoincrement=True)
    
    name = db.Column(db.Text, nullable=False)
    
    species = db.Column(db.Text, nullable=False)
    
    photo_url = db.Column(db.Text, nullable=True)
    
    age = db.Column(db.Integer, nullable=True)
    
    notes = db.Column(db.Text, nullable=True)
    
    available = db.Column(db.Boolean, nullable=False,
            default=True)
    
    def __repr__(self):
        return f"<Pet name={self.name} species={self.species} available={self.available}>"
    
    def get_pets():
        return Pet.query.all()
        
    def get_pet(id):
        return Pet.query.get_or_404(id)
    
    def add_pet(details):
        ...
        
    def edit_pet(detail):
        ...
        
    def delete_pet(id):
        ...