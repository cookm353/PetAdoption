from models import Pet, db
from app import app


def main():
    db.drop_all()
    db.create_all()

    Pet.query.delete()
    
    tom = Pet(name='Tom', species='Cat', 
              photo_url='static/images/maine_coon.jpg', age=4,
              notes='Playful Maine coon', available=True)
    emma = Pet(name='Emma', species='Dog', 
               photo_url='static/images/bohemian-shepherd.jpg', age=3,
               notes='Bohemian shepherd', available=True)
    terry = Pet(name='Terry', species='Porcupine',
                photo_url='static/images/porcupine.jpg',
                notes="A bit prickly at first, but quickly warms up",
                age=4, available=True)
    
    db.session.add_all([tom, emma, terry])
    db.session.commit()
    
    
    
if __name__ == "__main__":
    main()