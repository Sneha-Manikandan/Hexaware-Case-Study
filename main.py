from Entity import Artwork,Artist,User,Gallery,User_Favorite_Artwork
from DAO import ArtworkService,ArtistService,UserService,GalleryService,UserFavoriteArtworkService

class MainMenu:  
    artwork_service=ArtworkService() 
    artist_service=ArtistService()
    user_service=UserService()
    gallery_service=GalleryService()
    user_favorite_artwork_service=UserFavoriteArtworkService()

    def artwork_menu(self):
            while True:
                print("""
                    1. View all artworks
                    2. Get Artwork by Id
                    3. Add artwork
                    4. Delete artwork
                    5. Update artwork
                    6. Exit
                    """)
                choice=int(input("Please choose what you want to do: "))
                if choice==1:
                    self.artwork_service.readArtwork()
                elif choice==2:
                    artworkId=int(input("Enter Artwork Id: "))
                    self.artwork_service.getArtworkById(artworkId)
                elif choice==3:
                    title=input("Enter the title of the artwork: ")
                    description=input("Enter the description of the artwork: ")
                    creationDate=input("When was the artwork created? : ")
                    medium=input("Enter the medium of the artwork: ")
                    imageURL=input("Give the url of the artwork: ")
                    new_artwork=Artwork(title,description,creationDate,medium,imageURL)
                    self.artwork_service.addArtwork(new_artwork)
                elif choice==4:
                    self.artwork_service.readArtwork()
                    artworkId=input("Enter the artworkId you want to remove: ")
                    self.artwork_service.removeArtwork(artworkId)
                elif choice==5:
                    self.artwork_service.readArtwork()
                    artworkId=input("Enter the ArtworkId you want to update: ")
                    title=input("Enter the title of the artwork: ")
                    description=input("Enter the description of the artwork: ")
                    creationDate=input("When was the artwork created? : ")
                    medium=input("Enter the medium of the artwork: ")
                    imageURL=input("Give the url of the artwork: ")
                    self.artwork_service.updateArtwork(artworkId,title,description,creationDate,medium,imageURL)
                elif choice==6:
                    print("Thank You !!!")
                    break
                else:
                    print("Enter correct choice")


    def artist_menu(self):
        while True:
            print("""
                  1. Display Artists
                  2. Add Artist
                  3. Remove Artist
                  4. Update Artist
                  5. Exit
                  """)
            choice=int(input("Enter the choice you want to do: "))
            if choice==1:
                self.artist_service.readArtist()
            elif choice==2:
                name=input("Enter Artist name: ")
                biography=input("Enter Artist biography: ")
                birthDate=input("Enter Artist birthdate: ")
                nationality=input("Enter Artist nationality: ")
                website=input("Enter Artist website: ")
                contactInformation=input("Enter Artist contact information: ")
                new_artist=Artist(name,biography,birthDate,nationality,website,contactInformation)
                self.artist_service.addArtist(new_artist)
            elif choice==3:
                self.artist_service.readArtist()
                artistId=int(input("Enter the Artist ID you want to remove: "))
                self.artist_service.removeArtist(artistId)
            elif choice==4:
                self.artist_service.readArtist()
                artistId=int(input("Enter the Artist ID you want to update: "))
                name=input("Enter Artist name: ")
                biography=input("Enter Artist biography: ")
                birthDate=input("Enter Artist birthdate: ")
                nationality=input("Enter Artist nationality: ")
                website=input("Enter Artist website: ")
                contactInformation=input("Enter Artist contact information: ")
                self.artist_service.updateArtist(artistId,name,biography,birthDate,nationality,website,contactInformation)
            elif choice==5:
                break
            else:
                print("Invalid")

    def user_menu(self):
        while True:
            print("""
                  1. Display User
                  2. Display User By Id
                  3. Add User
                  4. Remove User
                  5. Update User
                  6. Exit
                  """)
            choice=int(input("Enter the choice you want to do: "))
            if choice==1:
                self.user_service.readUser()
            elif choice==2:
                userId=int(input("Enter UserId: "))
                self.user_service.readUserById(userId)
            elif choice==3:
                username=input("Enter Username: ")
                password=input("Enter Password: ")
                email=input("Enter Email: ")
                firstName=input("Enter Firstname: ")
                lastName=input("Enter Lastname: ")
                dateOfBirth=input("Enter Date of Birth: ")
                profilePicture=input("Upload Picture: ")
                favoriteArtworks=input("Enter Favorite Artist Id: ")
                new_user=User(username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks)
                self.user_service.addUser(new_user)
            elif choice==4:
                self.user_service.readUser()
                userId=int(input("Enter the user ID you want to remove: "))
                self.user_service.removeUser(userId)
            elif choice==5:
                self.user_service.readUser()
                userId=int(input("Enter the User ID: "))
                username=input("Enter Username: ")
                password=input("Enter Password: ")
                email=input("Enter Email: ")
                firstName=input("Enter Firstname: ")
                lastName=input("Enter Lastname: ")
                dateOfBirth=input("Enter Date of Birth: ")
                profilePicture=input("Upload Picture: ")
                favoriteArtworks=input("Enter Favorite Artist Id: ")
                self.user_service.updateUser(userId,username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks)
            elif choice==6:
                break
            else:
                print("Invalid")

    def gallery_menu(self):
        while True:
            print("""
                1. Display Gallery
                2. Add Gallery
                3. Remove Gallery
                4. Update Gallery
                5. Exit
                """)
            choice = int(input("Enter the choice you want to do: "))
            if choice == 1:
                self.gallery_service.readGallery()
            elif choice == 2:
                name = input("Enter Gallery name: ")
                description = input("Enter Gallery description: ")
                location = input("Enter Gallery location: ")
                curator = input("Enter Gallery curator: ")
                openingHours = input("Enter Gallery opening hours: ")
                artistId = int(input("Enter Artist ID: "))
                self.gallery_service.addGallery(name, description, location, curator, openingHours, artistId)
            elif choice == 3:
                self.gallery_service.readGallery()
                galleryId = int(input("Enter the Gallery Id you want to remove: "))
                self.gallery_service.removeGallery(galleryId)
            elif choice == 4:
                self.gallery_service.readGallery()
                galleryID = int(input("Enter the Gallery ID you want to update: "))
                name = input("Enter Gallery name: ")
                description = input("Enter Gallery description: ")
                location = input("Enter Gallery location: ")
                curator = input("Enter Gallery curator: ")
                openingHours = input("Enter Gallery opening hours: ")
                artistID = int(input("Enter Artist ID: "))
                self.gallery_service.updateGallery(galleryID, name, description, location, curator, openingHours, artistID)
            elif choice == 5:
                break
            else:
                print("Invalid")

    def user_favorite_artwork_menu(self):
        while True:
            print("""
                1. Display Favorite Artwork
                2. Display Favorite Artwork by UserId
                3. Add Favorite Artwork
                4. Remove Favorite Artwork
                5. Exit
                """)
            choice = int(input("Enter the choice you want to do: "))
            if choice == 1:
                self.user_favorite_artwork_service.getUserFavoriteArtwork()
            elif choice == 2:
                self.user_favorite_artwork_service.getUserFavoriteArtwork()
                userId = input("Enter userId: ")
                self.user_favorite_artwork_service.getUserFavoriteArtworksbyId(userId)
            elif choice == 3:
                userId = input("Enter userId: ")
                artworkId = input("Enter artworkId: ")
                new_favoriteArtwork=User_Favorite_Artwork(userId,artworkId)
                self.user_favorite_artwork_service.addArtworkToFavorite(new_favoriteArtwork)
            elif choice == 4:
                userId = input("Enter userId: ")
                artworkId = input("Enter artworkId: ")
                self.user_favorite_artwork_service.removeArtworkFromFavorite(userId,artworkId)
            elif choice == 5:
                break
            else:
                print("Invalid")

def main():
    while True:
            print("""
                1. Artwork Management
                2. Artist Management
                3. User Management
                4. Gallery Management
                5. Favorite Artwork Management
                6. Exit
                """)
            choice=int(input("Please choose what you want to do: "))
            if(choice==1):
                main_menu.artwork_menu()
            elif(choice==2):
                main_menu.artist_menu()
            elif(choice==3):
                main_menu.user_menu()
            elif(choice==4):
                main_menu.gallery_menu()
            elif(choice==5):
                main_menu.user_favorite_artwork_menu()
            elif(choice==6):
                print("Thank You !!")
                main_menu.artwork_service.close()
                main_menu.artist_service.close()
                main_menu.user_service.close()
                main_menu.gallery_service.close()
                main_menu.user_favorite_artwork_service.close()
                break
            else:
                print("Invalid! Enter proper choice")
   
        

if __name__=="__main__":
    print("WELCOME TO VIRTUAL ARTWORK MANAGEMENT")
    main_menu=MainMenu()
    main()
    
