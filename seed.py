from app import app
from models import Pet, db

db.drop_all()
db.create_all()

DEFAULT_IMG_URL = "https://cdn.pixabay.com/photo/2022/10/15/21/23/cat-7523894_960_720.jpg"

whiskey = Pet(name='Whiskey', species="dog", age="baby",
              photo_url=DEFAULT_IMG_URL, notes="", available=True)
bowser = Pet(name='Bowser', species="dog", age="baby",
              photo_url=DEFAULT_IMG_URL, notes="", available=False)
spike = Pet(name='Spike', species="porcupine", age="baby",
              photo_url=DEFAULT_IMG_URL, notes="", available=True)
spencer = Pet(name='Spencer', species="porcupine", age="baby",
              photo_url=DEFAULT_IMG_URL, notes="", available=True)

db.session.add_all([whiskey, bowser, spike, spencer])
db.session.commit()
