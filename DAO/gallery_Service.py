from Util.DBConn import DBConnection
from abc import ABC,abstractmethod

class IGalleryService(ABC):
    @abstractmethod
    def readGallery(self):
        pass
    @abstractmethod
    def addGallery(self,new_artist):
        pass
    @abstractmethod
    def removeGallery(self,artistId):
        pass
    @abstractmethod
    def updateGallery(self,name, description, location, curator, openingHours, artistID):
        pass
class GalleryService(DBConnection):
    def readGallery(self):
        try:
            self.cursor.execute("select * from gallery")
            galleries=self.cursor.fetchall()
            for gallery in galleries:
                print(gallery)
 
        except Exception as e:
            print(e)

    def addGallery(self,new_gallery):
        try:
            self.cursor.execute("insert INTO Movies (name, description, location, curator, openingHours, artistID) VALUES(?,?,?,?,?,?)",
                        (new_gallery.name, new_gallery.description,new_gallery.location,new_gallery.curator,new_gallery.openingHours, new_gallery.artistID)
                        )
            
            self.conn.commit() 
        except Exception as e:
            print(e)
       
    def removeGallery(self,galleryName):
        try:
            self.cursor.execute("Delete FROM gallery WHERE galleryName=?",
                        (galleryName)
                        )
            
            self.conn.commit()
        except Exception as e:
            print(e)
       

    def updateGallery(self,name, description, location, curator, openingHours, artistID):
        try:
            self.cursor.execute("Update Movies SET ?,?,?,?,?,? WHERE galleryName LIKE ?",
                        (name, description, location, curator, openingHours, artistID)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)
            
