class Book:
    publisher = '元智'

    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return name + " is not found"

if __name__ == '__main__':
    book = Book()
    print(book.publisher)
    print(book.bookname)
    book.bookname = 'Python'  # 此物件屬性僅給 book 物件變數所指向的 Book() 物件擁有
    print(book.bookname)

    book2 = Book()
    print(book2.publisher)
    print(book2.bookname)