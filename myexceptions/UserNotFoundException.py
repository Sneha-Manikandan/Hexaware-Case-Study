

class UserNotFoundException(Exception):
    def  __init__(self,userId):
        super().__init__(f"No such user with UserID {userId} found.")