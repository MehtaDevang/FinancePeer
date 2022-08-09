from app.models import ApiUser

INCORRECT_STRINGS = ["", None]

def check_existence(string:str) -> bool:
    """
        function to check if the string is a valid input
    """

    if string in INCORRECT_STRINGS:
        return False
    
    return True

def create_new_user(username:str, password:str) -> ApiUser:
    
    try:
        user = ApiUser()
        user.username = username
        user.set_password(password)
        user.save()

        return user
    except Exception as e:
        print("Error occured in creating a new user")
        raise e
    