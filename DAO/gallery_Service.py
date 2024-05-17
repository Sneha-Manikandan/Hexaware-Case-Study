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
class GalleryService(IGalleryService,DBConnection):
    def readGallery(self):
        try:
            self.cursor.execute("select * from gallery")
            galleries=self.cursor.fetchall()
            for gallery in galleries:
                 print(gallery)
            return galleries
 
        except Exception as e:
            print(e)
            return None

    def addGallery(self,galleryId,name, description, location, curator, openingHours, artistId):
        try:
            self.cursor.execute("insert INTO gallery (galleryId,name, description, location, curator, openingHours, artistID) VALUES(?,?,?,?,?,?,?)",
                                (galleryId,name, description, location, curator, openingHours, artistId))
            
            self.conn.commit() 
            return galleryId
        except Exception as e:
            print(e)
            return None
       
    def removeGallery(self,galleryId):
        try:
            self.cursor.execute("Delete from artwork_gallery where galleryId=?",(galleryId))
            self.cursor.execute("Delete FROM gallery WHERE galleryId=?",(galleryId))                                   
            
            self.conn.commit()
        except Exception as e:
            print(e)
       

    def updateGallery(self,galleryId,name, description, location, curator, openingHours, artistID):
        try:
            self.cursor.execute("Update gallery SET name = ?, description = ?, location = ?, curator = ?, openingHours = ?, artistID = ? WHERE galleryId= ?",
                        (name, description, location, curator, openingHours, artistID,galleryId)
                        )
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
