class book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
    
    def display(self):
        print(f"Book Name: {self.name}, Author: {self.author}")
        
class ebook(book):
    def __init__(self,name,author,size):
        super().__init__(name,author)
        self.size = size
        
    def display(self):
        print(f"Ebook Name: {self.name}, Author: {self.author}, Size: {self.size} MB")
        
b1=book("The Great Gatsby","F. Scott Fitzgerald")
e1=ebook("1984","George Orwell",2.5)

b1.display()
e1.display()

class lms:
    books = []
    def __init__(self,book,address):
        self.book = book
        self.address = address
    def display(self, book):
        self.books.append(book)
        print(f"Book Name: {book.name}, Author: {book.author}, Address: {self.address}")   
        fnwef'
        fnwefnw
        fnwef'