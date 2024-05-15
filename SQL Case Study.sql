CREATE TABLE [Artwork] (
  [artworkID] int IDENTITY(1,1),
  [description] varchar,
  [title] varchar,
  [creationDate] date,
  [medium] varchar,
  [imageURL] varchar,
  [artistID] int,
  PRIMARY KEY ([artworkID]),
  FOREIGN KEY ([artistID]) REFERENCES Artist([artistID]) 
);

CREATE TABLE [Artist] (
  [artistID] int IDENTITY(1,1),
  [name] varchar,
  [biography] varchar,
  [birthDate] date,
  [nationality] varchar,
  [website] varchar,
  [contactInformation] varchar,
  PRIMARY KEY ([artistID])
);

CREATE TABLE [UserTable] (
  [userID] int IDENTITY(1,1),
  [username] varchar,
  [password] varchar,
  [email] varchar,
  [firstName] varchar,
  [lastName] varchar,
  [dateOfBirth] date,
  [picture] varchar,
  [favoriteArtworks] int,
  PRIMARY KEY ([userID])
);

CREATE TABLE [Gallery] (
  [galleryID] int IDENTITY(1,1),
  [name] varchar,
  [description] varchar,
  [location] varchar,
  [curator] varchar,
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

select * from UserTable
select * from User_Favorite_Artwork
select * from Gallery
select * from Artwork_Gallery
select * from Artist
select * from Artwork