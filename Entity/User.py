class User:
    def __init__(self,username, password, email, firstName, lastName, dateOfBirth, profilePicture, favoriteArtworks=[]):
        self.username = username
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.profilePicture = profilePicture
        self.favoriteArtworks = favoriteArtworks