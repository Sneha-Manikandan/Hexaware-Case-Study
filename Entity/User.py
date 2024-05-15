class User:
    def __init__(self, userID, username, password, email, firstName, lastName, dateOfBirth, profilePicture, favoriteArtworks=[]):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.profilePicture = profilePicture
        self.favoriteArtworks = favoriteArtworks