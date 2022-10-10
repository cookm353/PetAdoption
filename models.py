from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.sql as sql

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Class representing the pet table"""
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
        """Get all pets"""
        return Pet.query.order_by(Pet.id).all()
        
    def get_pet(id):
        """Get a single pet"""
        return Pet.query.get_or_404(id)
        
    def add_pet(pet_details):
        """Create a pet and add to DB"""
        pet = Pet(name=pet_details.get('name'), species=pet_details.get('species'),
                  photo_url=pet_details.get('photo_url'), age=pet_details.get('age'),
                  notes=pet_details.get('notes'), available=pet_details.get('isAvailable'))
        
        db.session.add(pet)
        db.session.commit()
        
    def edit_pet(pet, pet_details):
        """Edit pet and changes entry in DB"""
        for k, v in pet_details.items():
            if k == 'photo_url':
                pet.photo_url = v
            if k == 'notes':
                pet.notes = v
            if k == 'available':
                pet.available = v

        db.session.add(pet)
        db.session.commit()