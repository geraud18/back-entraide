from user import Users


class Society(Users):

    def __int__(self, name, email, password, created, active, image, activity_area):
        super().__int__(name, email, password, created, active, image)
        self.activity_area = activity_area
