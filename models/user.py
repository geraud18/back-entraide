from models.person import Person
from database import db


class Users(Person):
    def __init__(self):
        super().__init__()
        self._created = None
        self._image = None

    def to_json(self):
        return {
            'name': self._name,
            'firstname': self._firstname,
            'email': self._email,
            'password': self._password,
            'created': self._created,
            'image': self._image,
            'telephone': self._telephone,
            'linkedin': self._linkedin
        }

    def save_user(self):
        result = db.users.insert_one(self.to_json())
        return str(result.inserted_id)

    @classmethod
    def all_user(cls):
        return db.users.find()

    @classmethod
    def find_user_by_email(cls, emails):
        return db.users.find_one({'email': emails})

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created):
        self._created = created

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

