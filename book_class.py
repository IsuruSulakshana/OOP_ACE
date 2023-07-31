class Book:
    def __init__(self, title, author):
        print("Book Info")
        self.title = title
        self.author = author
        
    def display_Info(self):
        print("Title", self.title)
        print("Author", self.author)
            
book = Book("The Jungle", "Tom")
book.display_Info()