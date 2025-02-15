import re
import random
import datetime

class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = UserUtil.generate_email(name, surname, "example.com")
        self.password = UserUtil.generate_password()
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}, Birthday: {self.birthday.strftime('%Y-%m-%d')}"

    def get_age(self):
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id].__dict__.update(user_update.__dict__)

    @classmethod
    def get_number(cls):
        return len(cls.users)

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.datetime.now().year)[-2:]
        random_suffix = str(random.randint(100000, 999999))
        return int(year_prefix + random_suffix)

    @staticmethod
    def generate_password():
        import string
        characters = string.ascii_letters +string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(characters) for _ in range(8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any (c.isdigit() for c in password) and any(c in "!@#$%^&*()-_=+" for c in password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]{2,}$"
        return bool(re.match(pattern, email))
