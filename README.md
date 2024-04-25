# E-Library

---
E-Library is a web-based application designed to provide a comprehensive platform for managing and accessing a digital library. 
The application is built using Django and JavaScript, with package management handled by pip for Python and npm for 
JavaScript.

The application allows users to browse through a vast collection of digital books, each associated with its respective author. 
Users can also borrow and return books, providing a dynamic and interactive library experience.

The application has two main user roles: User and Administrator. 
A User can browse the library, borrow books, and return them when finished. An Administrator, on the other hand, 
has the ability to add, delete, and modify books and authors in the library, providing comprehensive management of the 
library's content.

The application ensures secure user authentication and role-based access to various features. 
It also includes robust error handling and user notifications for a smooth user experience.

The project uses a PostgreSQL database for data storage, managed through Django's ORM. 
It also leverages Cloudinary for efficient and scalable media management.

The application's user interface is designed to be intuitive and user-friendly, ensuring a seamless user experience.

---
[View the live project here](https://pp4-library-f562eb8422f8.herokuapp.com)

![Responsive design](static/img/readme/smartphones.png)

![Responsive design](static/img/readme/desktop.png)


## Features 


### Existing Features

- __Books__
    - Administrator: 
        - View all books in the library.
        ![books admin](static/img/readme/books-admin.png) 
        - Add a new book to the library.
        - Edit an existing book in the library.
        - Delete a book from the library.    

    - User:

        - View all books in the library.

        ![books user](static/img/readme/books-user.png)
        - Borrow a book from the library.

        ![get book](static/img/readme/get-book.png)

        - Return a book to the library.

        ![return book](static/img/readme/return-book.png)

        - See if someone is reading the book.

      ![reading book](static/img/readme/reading-book.png)


- __Authors__
    - Administrator:
        - Add a new author to the library.
        - Edit an existing author in the library.
        - Delete a author from the library.
    - User:
        - Do not have access to see this page.
        - If a user tries to access this page, they will be redirected to the 403 page.

![403 page](static/img/readme/403.png)        