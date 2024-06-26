from Util.DBConn import DBConnection
from abc import ABC,abstractmethod
from myexceptions import GalleryNotFoundException


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

    def addGallery(self,name, description, location, curator, openingHours, artistId):
        try:
            self.cursor.execute("insert INTO gallery (name, description, location, curator, openingHours, artistID) OUTPUT inserted.galleryID VALUES(?,?,?,?,?,?)",
                                (name, description, location, curator, openingHours, artistId))
            
            new_gallery_id = self.cursor.fetchone()[0]
            self.conn.commit() 
            return new_gallery_id
        except Exception as e:
            print(e)
            return None
       
    def removeGallery(self,galleryId):
        try:
            self.cursor.execute("SELECT * FROM Gallery WHERE galleryID = ?", (galleryId))
            gallery = self.cursor.fetchone()
            if gallery is None:
                raise GalleryNotFoundException(galleryId)
            else:
                self.cursor.execute("Delete from artwork_gallery where galleryId=?",(galleryId))
                self.cursor.execute("Delete FROM gallery WHERE galleryId=?",(galleryId))                                   
                
                self.conn.commit()
        except GalleryNotFoundException as e:
            print("Error!!",e)
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
