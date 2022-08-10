from app.models import ApiUser, File

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
    
def add_json_to_db(name:str, data:dict, username:str):
    user = ApiUser.objects.get(username=username)
    file_obj = File()
    file_obj.name = name 
    file_obj.uploaded_by = user
    file_obj.content = data
    file_obj.save()
