from person import Person


class Admin(Person):

    def __init__(self, name, firstname, email, password):
        super().__init__(name, firstname, email, password)
