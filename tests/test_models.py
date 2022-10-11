from unittest import TestCase
from werkzeug.exceptions import NotFound
from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class Test_Pet(TestCase):
    def setUp(self):
        Pet.query.delete()
        lucy = Pet(name='Lucy', species='Cat', age=2, available=False,
                   notes='Very vocal and affectionate')
        
        db.session.add(lucy)
        db.session.commit()
        
        self.lucy = lucy
        
    def tearDown(self):
        db.session.rollback()
        
    def test_get_pet(self):
        """Test getting an individual pet"""
        pet = Pet.get_pet(1)
        self.assertEqual(pet.name, 'Lucy')
        
    def test_get_pet_404(self):
        """Make sure trying to get a non-existent pet raises a 404"""
        with self.assertRaises(NotFound):
            Pet.get_pet(2)
            
    def test_get_all_pets(self):
        """Test that we can retrieve all pets in DB"""
        pets = Pet.get_pets()
        lucy = pets[0]
        
        self.assertEqual(lucy.name, 'Lucy')
        
    def test_adding_pet(self):
        """Make sure we can add a pet"""
        Pet.add_pet({'name':'Buster', 'species': 'Dog', 'available': False})
        
        buster = Pet.get_pet(2)
        self.assertEqual(buster.name, 'Buster')
        
    def test_editting_pet(self):
        """Make sure we can edit a pet"""
        lucy = Pet.get_pet(1)
        Pet.edit_pet(lucy, {'available': True})
        
        self.assertEqual(lucy.available, True)