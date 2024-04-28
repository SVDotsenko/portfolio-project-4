на мобильном устройстве изменить ширину toast
добавить тоасты для всего что можно поменять 403, 404
проверить все роуты к которым у пользователя не должно быть доступов

сделать диаграмму моделей и их связей

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
[View live project here](https://pp4-library-f562eb8422f8.herokuapp.com)

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
      
          ![delete book](static/img/readme/delete-book.png)

        - The book must be return before deleting or editing.
      
          ![reading book](static/img/readme/delete-book-tooltip.png)
  
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
     ![authors admin](static/img/readme/authors-admin.png)
        - Add a new author to the library.
        - Edit an existing author in the library.
        - Delete an author from the library.
      
          ![delete book](static/img/readme/delete-author.png)
        - See if the book is taken by any reader.
          
    - User:
        - Do not have access to see this page.
        - If a user tries to access this page, they will be redirected to the 403 page.

          ![403 page](static/img/readme/403.png)        

- __My Profile__
    - Administrator:
      ![admin profile](static/img/readme/profile-admin.png)
        - Edit information about itself:
          - First name.
          - Last name.
          - Email.
          - Profile image
    - User:
      ![admin profile](static/img/readme/profile-user.png)
        - See the books that are currently reading.
        - Edit information about itself:
            - First name.
            - Last name.
            - Email.
            - Profile image.
        - Simulate error on server to see how work error handling for 500 error.        

### Features Left to Implement
- Protection of routes by roles through decorators.
- Make a check so that you cannot enter the same title of a book by the same author twice.
- Pagination, if there is a lot of content.
- Use ajax to avoid page reloading.
- Returning a book from the profile page.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.


### Validator Testing

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS


### Unfixed Bugs

- баг с модальным окном навбар увеличивается
- могут быть неиспользуемые цсс-классы


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub)


## Credits

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
http://www.tooplate.com/view/2108-dashboard