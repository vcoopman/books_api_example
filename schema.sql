DROP TABLE IF EXISTS book;

CREATE TABLE book (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  autor TEXT NOT NULL,
  language TEXT NOT NULL
 );

INSERT INTO book(id, name, autor, language) VALUES
(1, "Illusions: The Adventures of a Reluctant Messiah", "Richard Bach", "English");
