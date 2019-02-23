def klasterizing(books):
    group1=[]
    group2=[]
    for book in books:
        if book.size>700:
            group1.append(book)
            print('Tiazholaia kniga')
        else:
            group2.append(book)
            print('Legkaia kniga')

class Book:
    def __init__(self, theAuthor, theGenre, theSize):
        self.author=theAuthor
        self.genre=theGenre
        self.size=theSize
    def __str__(self):
        return self.author+'/'+self.genre

Book1=Book('Dostoevski','Drama',1500)
Book2=Book('Dostoevski','Drama',1630)
Book3=Book('Pushkin','Kriminal',300)

books=[]
books.append(Book1)
books.append(Book2)
books.append(Book3)

klasterizing(books)
print(Book1)