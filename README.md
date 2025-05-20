BOOK LIBRARY & RECOMMENDATION SYSTEM

Description
A console-based book catalog for adding, viewing, rating, searching, and content-based recommendations by author/genre.

Features
	•	Add Book: title, author, genre
	•	View Books: alphabetical list
	•	Rate Book: assign a 1–5 rating
	•	Search: prefix search on titles via a Trie
	•	Recommendations: +1 for matching genre, +1 for matching author, normalized by user ratings

Prerequisites
Python 3.6 or newer

Installation
	1.	Place main.py in a folder.
	2.	Ensure books.json exists or let the script create it on first run.

Usage
Run python main.py and choose from:
	1.	Add a book
	2.	View your books
	3.	Rate a book
	4.	Search for a book
	5.	Get recommendations
	6.	Exit

Data Storage
books.json holds an object with two keys, for example:
“books”: {
“The Hobbit”: { “author”: “J.R.R. Tolkien”, “genre”: “Fantasy” },
“1984”:       { “author”: “George Orwell”,    “genre”: “Dystopian” }
},
“ratings”: {
“The Hobbit”: 5
}

File Layout
	•	main.py
	•	books.json
