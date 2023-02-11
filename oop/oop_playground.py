# NOTE
# TODO

# Making an object of the class string that returns "Book"
# Some people say that a method is class specific function.

# class Book:

#     def __init__(self, title, author, pages, current_page):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = current_page
#         self.bookmark = 1

#     def bookmark_page(self):
#         self.bookmark = self.current_page

#     def turn_page(self):
#         self.current_page += 1

#     def __str__(self):
#         return f"Title:{self.title}, Author:{self.author}"

#     def __str__(self):
#         return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages} "

#     def __len__(self):
#         return self.pages


# my_book = Book("A great Book", "me", 198, 1)
# print(my_book)

###################################################################

# Add a method to turn back a page OR modify the turn_page method to go back or forwards based on a boolean parameter.

class Book:

    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1
        self.boolean = True

    def bookmark_page(self):
        self.bookmark = self.current_page

    def turn_page(self):
        self.current_page += 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, pages: {self.pages}"

    def __len__(self):
        return self.pages

    def go__page__back(self):
        self.current_page -= 1


my_book = Book("A great book", "me", 198, 1)
print(my_book)

my_book.bookmark_page()
print(my_book.bookmark)
my_book.turn_page()
my_book.bookmark_page()
print(my_book.bookmark)

my_book.go__page__back()  # Calling the method to turning the page back.
my_book.bookmark_page()
print(my_book.bookmark)

# Using
# if my_book.boolean:  # It's
#     my_book.turn_page()
#     my_book.bookmark_page
#     print(my_book.bookmark)
# else:
#     my_book.turn_page()
#     my_book.bookmark_page()
#     print(my_book.bookmark)

###################################


class Employee:

    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.start_date = start_date
        self.phone_number = phone_number

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return (self.name, self.phone_number)


employee_1 = Employee("Fran", 7800, "12345678", "1st June 2020")

print(employee_1.get_employment_details())
