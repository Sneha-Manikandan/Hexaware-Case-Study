
CREATE TABLE [Artist] (
  [artistID] int IDENTITY(1,1),
  [name] varchar(255),
  [biography] varchar(255),
  [birthDate] date,
  [nationality] varchar(255),
  [website] varchar(255),
  [contactInformation] varchar(255),
  PRIMARY KEY ([artistID])
);



CREATE TABLE [Artwork] (
  [artworkID] int IDENTITY (1,1),
  [title] varchar(255),
  [description] varchar(255),
  [creationDate] date,
  [medium] varchar(255),
  [imageURL] varchar(255),
  PRIMARY KEY ([artworkID]),
);



CREATE TABLE [UserTable] (
  [userID] int IDENTITY(1,1),
  [username] varchar(255),
  [password] varchar(200),
  [email] varchar(255),
  [firstName] varchar(200),
  [lastName] varchar(200),
  [dateOfBirth] date,
  [profilePicture] varchar(255),
  [favoriteArtworks] int,
  PRIMARY KEY ([userID])
);

CREATE TABLE [Gallery] (
  [galleryID] int IDENTITY(1,1) ,
  [name] varchar(200),
  [description] varchar(255),
  [location] varchar(255),
  [curator] varchar(255),
  [openingHours] time,
  [artistID] int,
  PRIMARY KEY ([galleryID]),
  FOREIGN KEY ([artistID]) REFERENCES Artist([artistID])
);

CREATE TABLE [User_Favorite_Artwork] (
  [userID] int,
  [artworkID] int,
  FOREIGN KEY ([userID]) REFERENCES UserTable([userID]),
  FOREIGN KEY ([artworkID]) REFERENCES Artwork([artworkID])
);

CREATE TABLE [Artwork_Gallery] (
  [artworkID] int,
  [galleryID] int,
  FOREIGN KEY ([artworkID]) REFERENCES Artwork([artworkID]),
  FOREIGN KEY ([galleryID]) REFERENCES Gallery([galleryID])
);

