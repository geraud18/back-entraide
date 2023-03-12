from user import Users


class Particular(Users):

    def __int__(self, name, email, password, created, active, image, username, level_of_experience):
        super().__int__(name, email, password, created, active, image)
        self.username = username
        self.level_of_experience = level_of_experience

