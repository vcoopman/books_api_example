DROP TABLE IF EXISTS book;

CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `autor` varchar(255) NOT NULL,
  `language` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
 );

INSERT INTO book(id, name, autor, language) VALUES
(1, "Illusions: The Adventures of a Reluctant Messiah", "Richard Bach", "English");
