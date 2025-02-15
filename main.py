from userClassMethods import UserUtil
from userClassMethods import User
from userClassMethods import UserService

if __name__ = "__main__":
    birthday = datetime.date(2006, 1, 22)
    user = User(UserUtil.generate_user_id(), "Nursezim", "Alieva", birthday)
    UserService.add_user(user)
    print(user.get_details())
    print("Age:", user.get_age())
    print("Valid email:", UserUtil.validate_email(user.email))