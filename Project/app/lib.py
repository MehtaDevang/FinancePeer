from app.models import ApiUser, File
import pickle

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

def get_uploaded_files(username:str):
    files = File.objects.filter(uploaded_by__username=username)
    print(files)

    file_details = []
    for file in files:
        file_details.append({
            "file_name": file.name,
            "upload_date" : file.upload_date
        })

    return file_details

def get_file_content(username:str, file_name:str):
    file = File.objects.get(uploaded_by__username = username, name=file_name)
    content = file.content
    return content