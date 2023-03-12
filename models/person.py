class Person:

    def __init__(self):
        self._name = None
        self._firstname = None
        self._email = None
        self._telephone = None
        self._linkedin = None
        self._password = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        self._telephone = telephone

    @property
    def linkedin(self):
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        self._linkedin = linkedin

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
