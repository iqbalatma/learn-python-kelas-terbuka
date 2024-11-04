listBooks = []
while True :
    print("Please enter your book data")
    title = input("Please enter your book title: ")
    author = input("Please enter your book author: ")

    newBook = [title, author]
    listBooks.append(newBook)

    print("NO.\t| Title \t\t| Author")
    for index, book in enumerate(listBooks) :
        print(f"{index}\t| {book[0]}\t\t\t| {book[1]}")

    isContinue = input("Do you want to continue (y/n)")
    if isContinue.upper() == "N" :
        break

print("Program Finished")


