from unittest import TestCase
from app import app
from models import Pet, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_test'
app.config['SQLALCHEMY_ECHO'] = False
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
            
            
    # def test_add_pet_form(self):
    #     with app.test_client() as client:
    #         resp = client.get('/add')
    #         html = resp.get_data(as_test=True)
            
    #         self.assertEqual(resp.status_code, 200)
            
    
    # def test_adding_pet(self):
    #     with app.test_client() as client:
    #         data = {}
    #         resp = client.post('/add', follow_redirects=True)
    #         html = resp.get_data
            
    #         self.assertEqual(resp.status_code, 200)