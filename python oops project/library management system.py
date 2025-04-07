class library:
    def __init__(self):
        self.__ava_books=["python","java","ds","html","css","javascript"]

    def borrow_books(self,bor_book):
        if bor_book not in self.__ava_books:
            print(f"{bor_book} Book is not availabe !! choose display to see available books.")
        else:
            self.__ava_books.remove(bor_book)
            print(f"You have borrowed {bor_book}, Enjoy reading.....")

    def return_book(self,ret_book):
        self.__ava_books.append(ret_book)
        print(f"Thanks for returning {ret_book}")

    def display(self):
        print("Available Books :")
        for books in self.__ava_books:
            print(f" - {books}")

p1=library()
while True:
    op=int(input('''Choose an option :
    1. Look into available books
    2. Borrow a book
    3. Return a book
    4. Exit '''))

    if op==1:
        p1.display()
    elif op==2:
        bor_book=input("Which book you want to borrow :")
        p1.borrow_books(bor_book)
    elif op==3:
        ret_book=input("What is the book you are returning :")
        p1.return_book(ret_book)
    elif op==4:
        print("Exited sucessfully.....Thank you")
        break
    else:
        print("choose option correctly")




