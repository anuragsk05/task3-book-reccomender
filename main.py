import json
import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        # Helper function to perform DFS and collect words
        def dfs(node, prefix, results):
            if node.is_end_of_word:
                results.append(prefix)
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char, results)

        # Find the node where the prefix ends
        node = self.root
        for char in word:
            if char not in node.children:
                return []  # Return an empty list if the prefix is not found
            node = node.children[char]

        # Perform DFS from the node to collect all words
        results = []
        dfs(node, word, results)
        return results
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            self.dfs(child_node, prefix + char, results)
    
def load_books():
    if os.path.exists('books.json'):
        with open('books.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def view_books(books):
    # Display the list of books in alphabetical order by title
    print("\nYour Books:")
    for title in sorted(books.keys(), key=lambda x: x.lower()):
        book = books[title]
        print(f"- {title} - Author: {book['author']} - Genre: {book['genre']}")

def main():
    print("Welcome to the book catalog!\n")
    choice = ''
    while choice != '6':
        print("-- Menu --")
        print("Please enter a number to select an option:")
        print("1. Add a book")
        print("2. View your books")
        print("3. Rate a book")
        print("4. Search for a book")
        print("5. Get Recommendations")
        print("6. Exit")

        file = load_books()  # Correctly call the function
        books = file['books']
        ratings = file['ratings']
        trie = Trie()
        for title in books.keys():
            trie.insert(title.lower())  # Use the title as the key
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            book_name = input("Enter the book name: ")
            author = input("Enter the author name: ")
            genre = input("Enter the genre: ")
            books[book_name] = {"author": author, "genre": genre}
            with open('books.json', 'w') as file:
                json.dump({"books": books, "ratings": ratings}, file, indent=4)
            print(f"Book '{book_name}' added successfully!")
            
        elif choice == '2':
            if books:
                view_books(books)
            else:
                print("No books found.")
        elif choice == '3':
            book_name = input("Enter the book name to rate: ")
            rating = int(input("Enter your rating (1-5): "))
            if book_name in books:
                ratings[book_name] = rating
                with open('books.json', 'w') as file:
                    json.dump({"books": books, "ratings": ratings}, file, indent=4)
                print(f"Book '{book_name}' rated successfully!")
            else:
                print(f"Book '{book_name}' not found.")
        elif choice == '4':
            book_name = input("Enter the book name to search: ")
            search_results = trie.search(book_name.lower())
            if search_results:
                print("\nSearch Results:")
                for result in search_results:
                    print(f"- {result.title()}")
            else:
                print(f"No books found matching '{book_name}'.")
                
        elif choice == '5':
            scores = {}
            for rated_book, rating in ratings.items():  # Iterate over rated books and their ratings
                for book_title, book_details in books.items():  # Iterate over all books in the database
                    if book_title.lower() == rated_book.lower():
                        continue  # Skip already rated books
                    if book_title not in scores:
                        scores[book_title] = 0
                    # Compare genres and authors to calculate scores
                    rated_book_details = books[rated_book]
                    if book_details['genre'] == rated_book_details['genre']:
                        scores[book_title] += 1
                    if book_details['author'] == rated_book_details['author']:
                        scores[book_title] += 1
            
            # Adjust scores based on ratings
            for book_title in scores.keys():
                if book_title in ratings:
                    scores[book_title] *= (ratings[book_title] / 5)  # Normalize by rating
            
            # Sort by score and display recommendations
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            print("\nRecommendations:")
            if sorted_scores:
                n = 0
                for book, score in sorted_scores:
                    if score > 0.5: 
                        print(f"- {book}, Author: {books[book]['author']}, Genre: {books[book]['genre']}")
                        n += 1
                    if n >= 5:
                        print("\n")
                        break
            else:
                print("No recommendations available.")

        elif choice == '6':
            print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()