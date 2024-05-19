from myexceptions import UserNotFoundException
from Util.DBConn import DBConnection
from abc import ABC,abstractmethod

class IUserService(ABC):
    @abstractmethod
    def readUser(self):
        pass
    @abstractmethod
    def addUser(self,new_user):
        pass
    @abstractmethod
    def removeUser(self,userId):
        pass
    @abstractmethod
    def updateUser(self,userId,username,password,email,firstName,lastName,dateOfBirth,picture,favoriteArtworks):
        pass
class UserService(IUserService,DBConnection):

    def readUser(self):
        try:
            self.cursor.execute("select * from UserTable")
            users=self.cursor.fetchall()
            for user in users:
                print(user)
  
        except Exception as e:
            print(e)

    def readUserById(self,userId):
        try:
            self.cursor.execute("select * from UserTable where userId=?",(userId))
            user=self.cursor.fetchone()
            if user is None:
                raise UserNotFoundException(userId)
            else:
                print(user)
        except UserNotFoundException as e:
            print("Error!!",e)
        
        except Exception as e:
            print(e)

    def addUser(self,new_user):
        try: 
            self.cursor.execute("Insert INTO userTable (username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks) VALUES(?,?,?,?,?,?,?,?)",
                            (new_user.username,new_user.password,new_user.email,new_user.firstName,new_user.lastName,new_user.dateOfBirth,new_user.profilePicture,new_user.favoriteArtworks)
                            )
                
            self.conn.commit()  
        except Exception as e:
            print(e)
       

    def removeUser(self,UserId):
        try:
            self.cursor.execute("SELECT * FROM UserTable WHERE userID = ?", (UserId))
            user = self.cursor.fetchone()
            if user is None:
                raise UserNotFoundException(UserId)
            else:
                self.cursor.execute("Delete FROM userTable WHERE userId=?",
                            (UserId)
                            )
                
                self.conn.commit()
        except UserNotFoundException as e:
            print("Error!!",e)       
        except Exception as e:
            print(e)
       

    def updateUser(self,userId,username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks):
        try:
            self.cursor.execute("Update UserTable SET username = ?, password = ?, email = ?, firstName = ?, lastName = ?, dateOfBirth = ?, profilePicture = ?, favoriteArtworks = ? WHERE userId=?",
                        (username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks,userId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)
            
