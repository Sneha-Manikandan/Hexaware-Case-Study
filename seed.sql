
INSERT INTO [Artist] ([name], [biography], [birthDate], [nationality], [website], [contactInformation])
VALUES
( 'Salvador Dalí', 'Spanish surrealist artist renowned for his technical skill and striking, bizarre images.', '1904-05-11', 'Spanish', 'https://www.salvadordali.com', 'contact@salvadordali.com'),
( 'Georgia O Keeffe', 'American modernist artist known for her paintings of enlarged flowers, New York skyscrapers, and New Mexico landscapes.', '1887-11-15', 'American', 'https://www.georgiaokeeffe.net', 'contact@georgiaokeeffe.net'),
( 'Henri Matisse', 'French artist known for his use of color and his fluid and original draughtsmanship.', '1869-12-31', 'French', 'https://www.henrimatisse.org', 'contact@henrimatisse.org'),
('Andy Warhol', 'American artist, film director, and producer who was a leading figure in the visual art movement known as pop art.', '1928-08-06', 'American', 'https://www.warhol.org', 'contact@warhol.org'),
('Rembrandt', 'Dutch draughtsman, painter, and printmaker, one of the greatest visual artists in the history of art and the most important in Dutch art history.', '1606-07-15', 'Dutch', 'https://www.rembrandthuis.nl', 'contact@rembrandthuis.nl');


INSERT INTO [Artwork]( [title],[description], [creationDate], [medium], [imageURL])
VALUES
( 'A painting by Salvador Dalí', 'The Persistence of Memory', '1931-01-01', 'Oil on canvas', 'https://example.com/persistenceofmemory.jpg'),
( 'A painting by Georgia O Keeffe', 'Red Canna', '1924-01-01', 'Oil on canvas', 'https://example.com/redcanna.jpg'),
('A painting by Henri Matisse', 'The Dance', '1910-01-01', 'Oil on canvas', 'https://example.com/thedance.jpg'),
('A painting by Andy Warhol', 'Campbell Soup Cans', '1962-01-01', 'Synthetic polymer paint on canvas', 'https://example.com/campbellssoupcans.jpg'),
('A painting by Rembrandt', 'The Night Watch', '1642-01-01', 'Oil on canvas', 'https://example.com/thenightwatch.jpg');


INSERT INTO [UserTable] ([username], [password], [email], [firstName], [lastName], [dateOfBirth], [profilePicture], [favoriteArtworks])
VALUES
('artlover2', 'password6', 'artlover2@example.com', 'Sarah', 'Brown', '1988-06-06', 'https://example.com/sarahbrown.jpg', 1),
('artenthusiast3', 'password7', 'artenthusiast3@example.com', 'Daniel', 'Williams', '1992-07-07', 'https://example.com/danielwilliams.jpg', 2),
('artcollector4', 'password8', 'artcollector4@example.com', 'Laura', 'Martinez', '1984-08-08', 'https://example.com/lauramartinez.jpg', 3),
('gallerygoer5', 'password9', 'gallerygoer5@example.com', 'Peter', 'Garcia', '1990-09-09', 'https://example.com/petergarcia.jpg', 4),
('artappreciator6', 'password10', 'artappreciator6@example.com', 'Emma', 'Taylor', '1986-10-10', 'https://example.com/emmataylor.jpg', 5);



INSERT INTO [Gallery] ([name], [description], [location], [curator], [openingHours], [artistID])
VALUES
('Dalí Theatre and Museum', 'Museum dedicated to Salvador Dalí in his home town of Figueres, in Catalonia, Spain.', 'Figueres, Spain', 'Salvador Dalí', '09:00:00', 1),
('Georgia O Keeffe Museum', 'Museum dedicated to the artistic legacy of Georgia O Keeffe.', 'Santa Fe, New Mexico, USA', 'Georgia O Keeffe', '10:00:00', 2),
('Matisse Museum', 'Museum dedicated to the works of Henri Matisse.', 'Nice, France', 'Henri Matisse', '11:00:00', 3),
('The Andy Warhol Museum', 'Museum dedicated to the works of Andy Warhol.', 'Pittsburgh, Pennsylvania, USA', 'Andy Warhol', '12:00:00', 4),
('The Rembrandt House Museum', 'Historic house and art museum in Amsterdam, Netherlands, dedicated to the work of Rembrandt.', 'Amsterdam, Netherlands', 'Rembrandt', '13:00:00', 5);


INSERT INTO [User_Favorite_Artwork] ([userID], [artworkID])
VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 3),
(4, 4),
(5, 5);


INSERT INTO [Artwork_Gallery] ([artworkID], [galleryID])
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
