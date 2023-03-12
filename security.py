from werkzeug.security import safe_str_cmp
from models.user import Users


def authenticate(username, password):
    users = Users()