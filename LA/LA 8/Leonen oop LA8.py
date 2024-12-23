class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
book1 = book("juan tamad", "leanne")
del book1.author
#print(book1.title, book1.author)

book2= book("ako may lobo", "faith")
print(book2.title, book2.author)