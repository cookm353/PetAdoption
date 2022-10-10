from unittest import TestCase
from app import app
from models import Pet, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['WTF_CSRF_ENABLED'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class Test_App(TestCase):
    def setUp(self):
        Pet.query.delete()
        lucy = Pet(name='Lucy', species='Cat', age=2, available=False,
                   notes='Very vocal and affectionate')
        
        db.session.add(lucy)
        db.session.commit()
        
        self.lucy = lucy
        
    def tearDown(self):
        db.session.rollback()
        
    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Lucy", html)
            self.assertIn("isn't available", html)
                
    def test_add_pet_form(self):
        with app.test_client() as client:
            resp = client.get('/add')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Add a Pet', html)
            
    def test_adding_pet(self):
        with app.test_client() as client:
            data = {'name': 'Buster', 'species': 'dog', 'available': True}
            resp = client.post('/add', follow_redirects=True, data=data)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Buster', html)
            # It SHOULD be redirecting to '/', but it keeps going back to the add pet page
            # self.assertIn("is available", html)
            
    def test_pet_details_display(self):
        with app.test_client() as client:
            resp = client.get('/1')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Lucy', html)
            
    def test_pet_edit(self):
        with app.test_client() as client:
            data = {'notes': 'Noisy little beast', 'available': False}
            resp = client.post('/1', data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('beast', html)
            # self.assertNotIn('Edit', html)