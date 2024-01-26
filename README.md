# The Muscle Factory- A Django project, for Code Institute
# General 
The Muscle Factory is a website that lets users register for an account, book appointments and provides information about upcoming events. The user can read about the services provided and the people working at The Muscle Factory. When the user has created and account he/she can manage their bookings with full CRUD functionality.
This means that the user can:
* Create a booking
* Review their bookings
* Update and edit bookings
* Delete their bookings

The user will be kept up to date with upcoming events that are managed by the admin panel. This is to always keep the website updated, and also attract new members with fun and creative events. 

The website is also equipped with a contact form where anyone can contact The Muscle Factory. This will also send an auto-reply to the user, to inform them that their message has been sent and is awaiting a reply. 

The website is designed to make the user feel welcome regardless of their workout history. Everyone is welcome to join and form a new healthy lifestyle with The Muscle Factory.

The idea that The Muscle Factory was based on is my sister´s personal trainer company: Reality Lift. This project is only a simple example of what a fitness company website could look like and what features that are necessary. This project will hopefully be the base for my sister´s companys website in the future.

Link to live website can be found here:
[Click Me](https://the-muscle-factory-9f171161969d.herokuapp.com/)

![Am I resppnsive](docs/readme%20docs/images/air.png)

## Table of Contents
- [#General](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#general)
- [## Table of Contents](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#table-of-contents)
- [Project Goals](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#project-goals)
- [UX](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#ux)
- [Development](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#development)
- [Flowchart](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#flowchart)
- [User Stories](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#user-stories)
- [Colors and Fonts](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#colors-and-fonts)
- [Wireframes](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#wireframes)
- [General Features](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#general-features)
- [Features](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#features)
- [Database](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#database)
- [Testing](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#testing)
- [Code Validation](https://github.com/ElinaBoman/the-muscle-factory?tab=readme-ov-file#code-validation)
- [Testing User Stories]()
- [Manuel Testing](https://github.com/ElinaBoman/the-muscle-factory/blob/main/docs/readme%20docs/README-TESTING.md)
- [Lighthouse Testing](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#lighthouse-testing)
- [Browswe Testing](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#browser-testing)
- [Future Improvments](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#future-improvements)
- [Bugs](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#bugs)
- [Technologies Used](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#technologies-used)
- [Libraries](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#libraries)
- [Packages](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#packages)
- [Framework and Websites](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#framework-and-websites)
- [Deployment](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#deployment)
- [Credits](https://github.com/ElinaBoman/the-muscle-factory/tree/main?tab=readme-ov-file#credits)


### Project Goals

The main goals for this project was:

* Create a website using Django Framework 

* Use: Bootstrap, python, javascript, CSS and HTML

* Create a website with full CRUD functionality

* Create a appealing frontend suiting a fitness website

* Use a database to store information about users and their appointments

* Set up email functionality and use auto-reply

## UX
The main goal for the website is to attract new members and also take care of member bookings. It was important that the website had a clean professional front. To make the website more interesting and also be able to show The Muscle Factorys mantra a Bootstrap Carousel was placed on the landing page. The carousel shows images of the gym, members and some healthy food to immediately let the user know what the website is all about. The first slide for example lets the user know that it's The Muscle Factorys mission to help members create a healthier lifestyle, but also how important it's to have a helpful community that supports members all the way.

### Development 
#### Agile Development Process
The Muscle Factory project was planned through user stories. These stories were created from a user and site owner perspective. The stories describe what the project should include and would set the overall planning structure.
One important part of this project was to use an agile development method. This would make the customer's perspective very important but since this is not a real project with real customers, user stories were made up by creating potential customers and site owners.
In agile development iterative and incremental development is a very important part. Each user story represents a smaller and easier to manage part of the project. This helped a lot with planning the workload.
As there was not a team building this project it might be hard to fully grasp the concept of agile development, since teamwork is a big part of that. Instead of having a team, I choose to create a chat group on Slack. Working with the criticism I got from fellow students, this turned out to be a very good idea. I got a lot of feedback that I later on implemented in my project, so big credits to my friends on Slack.
A Kanban board was created on GitHub to structure the project development. By taking all my user stories and labeling them with their significance for this project, it was a lot easier to assess each user story after their relevance.
Not all user stories were finished, but all user stories with the label "MUST HAVE" were completed.


[Click to view Kanban board](https://github.com/users/ElinaBoman/projects/5/views/1)

### Flowchart
To view project structure, see flowchart:
<details>
<summary>Lucidchart</summary>

![Lucidchart](docs/readme%20docs/images/lucidchart.png)
</details>

### User Stories
#### View User stories:

![User Stories](docs/readme%20docs/ux-testing/UX.png)

#### This is how the User stories have been implemented:
-  #2 As a user I can make bookings on the website so that I can plan my schedule

The user can create bookings and also view them on the website.

-  #3 As a user I can edit/delete bookings on the website so that I can change my schedule

There are options for the user to edit and delete their bookings.

-  #4 As a user I can create an account so I can see my bookings

There is a fully functioning authentication system so each user can view their own bookings and manage them.

-  #5 As a site owner I can create events so that I can display them on the website

In the admin panel the site owner can create events so that the website is always up to date.

-  #6 As a site owner I can edit events so that I can display changes on the website

The site owner can manage the events, including changing published events.

-  #7 As a site owner I can get in contact with clients so that I can connect with clients

There is a contact form on the website collecting user information entered by the user. The user can, of course, choose if they want to display their full name and phone number; only the name and email are required. User information is displayed in the admin panel.

-  #8 As a site owner I can delete events so that I can remove it from the website

The events can be deleted in the admin panel.

-  #9 As a user I can see available dates in a calendar so that I can schedule private sessions

The booking form will only show available dates and time in their widgets.

-  #10 As a site owner I can display pictures of the gym so I can attract more clients

This has not been fully completed. There is a picture of the gym in the Bootstrap carousel, but it's not clear enough that the image represents the gym. This would be a future implementation.

-  #11 As a site owner I can display and edit information about employees specialization so that I can attract more clients

This has not been completed. Even tough there is information about the employees, the admin does not have the ability to change this information yet. This would be a future implementation. 

-  #12 As a user I can use the website on my phone so that I can make, edit and delete bookings with ease from my phone

The website is fully responsive and all booking features works on all viewports.

-  #13 As a site owner I can display information on the website so that I can inform clients about services and events

All services are described on the website.

### Colors and Fonts
To create a clean and professional looking website calm colors were used. The main colors are gray but then there are some color pops to catch the eye of the user. This adds a bit of playfulness to the overall clinic looking front. Since this is a company that focuses more on the long term health of members with not only gym membership but also massage, rehab and dietist . It's more of a clinical gym and therefore the colors are more on the cool side. 

![Palette](docs/readme%20docs/images/colorpalette.png)

The fonts that are used are mainly clean and thin with dark colors. The headings are bold and thick creating a strong and sturdy look. The main text is balanced nicely with the thinner text creating an easy to read front. The font for heading has been borrowed from GoogleFonts, and the main text is set to the font of apple device's.
* Heading: Bebas Neue, fallback: sans-serif
* Main text: apple-system, fallback: sans-serif


### Wireframes
To plan the design and responsiveness of The Muscle Factory a tool called Balsamiq was used. This was in the early stages of the project and the images created do not represent the finished product. Balsamiq was used to visualize the project in different wireframes. 

<details>
    <summary>Smaller devices</summary>

![Small](docs/readme%20docs/wireframes/wireframes-sm-landing-about-contact.png)

![Small](docs/readme%20docs/wireframes/wireframes-sm-create-delete.png)
</details>

<details>
  <summary>Medium devices</summary>

![Medium](docs/readme%20docs/wireframes/wireframes-md-landing-about.png)

![Medium](docs/readme%20docs/wireframes/wireframes-md-contact.png)

![Medium](docs/readme%20docs/wireframes/wireframes-md-create-bookings.png)
</details>
<details>
 <summary>Large devices</summary>

![Large](docs/readme%20docs/wireframes/wireframes-lg-landing.png)

![Large](docs/readme%20docs/wireframes/wireframes-lg-about.png)

![Large](docs/readme%20docs/wireframes/wireframes-lg-contacts.png)

![Large](docs/readme%20docs/wireframes/wireframes-lg-create.png)

![Large](docs/readme%20docs/wireframes/wireframes-lg-delete.png)

</details>


##  General Features
The Muscle Factory website is divided between if a user is authenticated or not. To view the full front end website the user must be registered and signed in.

#### For a user who is not signed in following views available are:

- Home

Landing page: Any user can read about membership prices and view some inspirational paragraphs. There is also a button that will take unregistered users to the registration form.

- Registration:

Any user can sign up for an account. The user needs to enter username, email and password.
- Contact Us

Any user can send an email to The Muscle Factory. The contact form will send out an auto reply from The Muscle Factory.

- About Us

Information about the company is displayed here. The user can read about provided services and employees.

- Bookings

The bookings page will render different content depending on whether the user is authenticated or not. For a signed-in user, a booking form will allow the user to book services. If the user is not signed in, the bookings link will instead render the registration form.


#### For a user who is signed in, following views are avaialable:
- Home

Registration button is exchanged with a greeting to the user.
- Contact Us
- About Us
- Bookings: 
Bookings: When a user is authenticated, the bookings view will allow the user to enter a booking through a form. To submit the form, the user needs to:

    
    - Choose service. The services provided are Personal trainer, Rehab, Massage or Dietist.
    - Choose time and date. The time and date widgets will only show available dates and times. 
    - Enter if this is the users first appointment.
    - Extra comments, if there is anything the user would like to add, this field is not required.
- My Bookings

All bookings made by a user will be displayed, providing full CRUD functionality. If the user wants to delete a specific booking, the delete button will first render a view asking if the user really wants to delete the booking. If the user deletes the booking, an alert will inform the user that the chosen booking has been deleted.
If the user would like to edit a booking, the booking form renders with pre populated fields. If the user updated the booking there will be an alert informing user, that the booking has been updated.
If user wants to add a new booking from My Bookings view, the booking form will render.

- Logout

If a user signs out there is an alert message letting the user know if the event was successful.

### Features
### Header and Navigation
The header and navigation menu are responsive and will change to suit different wireframes. On bigger screens, the menu will display all navigation elements, but on smaller screens, the elements will be contained in a hamburger bar. The navbar also contains a kettlebell logo, same as in the title.
The navbar elements change depending on whether the user is signed in or not. For a user who is not signed in, the navigation elements are Home, About us, Contact us, and Booking. If the user is signed in, there will also be a link to My bookings.
![Header and Nav](docs/readme%20docs/images/features/header-navbar.png)
![Smaller nav](docs/readme%20docs/images/features/navbar-smaller.png)
![Nav bar collapsable](docs/readme%20docs/images/features/navbar.png)

### Home
The Home page is the landing page. This page contains a Bootstrap carousel with some pictures of the gym, members, and healthy food. This is to immediately describe the company to any user. The pictures are chosen because they resemble community and health. If the user is signed in, there will be a greeting displayed in the carousel. If a user is not signed in, there will instead be a 'Join us now' button that will take the user to the registration form. This is to have as few steps as possible between entering the website and getting users to sign up. The user does not need to look for the registration form since it's the first button on the landing page.

After the carousel, there is some informative text about the company and also the different memberships available.

The user can then read about upcoming events that are posted by the admin. Here fun and creative events are displayed. Not only describing training events but also social events since The Muscle Factory is all about creating a community with a supportive environment between members and employees. The events are clickable and will render more information about the event.

![Index](docs/readme%20docs/images/features/index-medals.png)
![Index](docs/readme%20docs/images/features/events-index.png)

### Footer
The footer has the same information on all pages. It contains opening hours, address, and links to social media. The footer is responsive and will change to fit different wireframes.
![Index](docs/readme%20docs/images/features/footer.png)

### Register
The Register/Sign up page collects Username, email address, and password. There is also a link to go directly to sign in, which will render the login form. There is information that describes criteria for selecting a password, making it easier for the user to create an account. The form is a part of Django's built-in allauth templates but has been styled to suit this project.
![Signup](docs/readme%20docs/images/features/signup.png)

### About us
The 'About Us' page briefly describes The Muscle Factory's services and employees. The main reason to have this page was to create a more personal connection to users. For a person who has never been to The Muscle Factory, it might seem scary to go to a new gym. In order to make new users feel more comfortable, the pictures of the employees show friendly faces. The description of services is made to make the user feel more secure and let them know that the services are personalized and unique to each user.
![About](docs/readme%20docs/images/features/aboutus.png)

### Contact us
The Contact Us page provides a form for any user to reach out. The form will be stored in the database where the admin can view them in Django's built-in Admin panel. The form will also send an email to The Muscle Factory's email account, and the user will receive an auto-reply. There is also an alert message informing the user of success or errors with the form. The fields collected are Name, Last name, Phone number, Email, and Message. The user can choose if they want to fill out the whole form. Only Name, Email, and Message are required.
![Database Models](docs/readme%20docs/images/features/contact-form.png)

### Bookings
If a user has not signed in, the Bookings link will instead take the user to the registration form. For a user who is signed in, there will be a form to create a booking. The form fields are Event date, Start time, Event choice. There is also a question if this is the user's first appointment. Lastly, the user can add information if there is anything they would like to add. The form will be saved to the database, where the admin can view bookings and approve appointments in the admin panel.
![Bookings](docs/readme%20docs/images/features/create-booking.png)

### My bookings
My bookings will be available to signed-in users. Here the user can view their bookings. The user can also choose to Edit, Delete, or Add their bookings.
![My bookings](docs/readme%20docs/images/features/madebookings.png)

### Login
If a user is registered, they can log in. This is a part of Django's built-in allauth forms. The user can choose to enter 'Remember me' to make future sign-ins easier. If the user does not have an account yet, there is a link to the registration form. When the user has successfully signed in, there will be an alert message.
![Login](docs/readme%20docs/images/features/signin.png)

### Logout
The logout page is for the user to sign out. Before a user can sign out, they have to confirm their action. If the user confirms that they want to sign out, the user will be logged out, and an alert message will confirm the action.
![Login](docs/readme%20docs/images/features/signout.png)


## Database
To store user information a relational database was used called PostgreSQL. The database is managed through ElephantSQL. Read more about ElephantSQL in the deployment section.

#### The project contains four apps: User(AllAuth), Blog, Bookings and Contact.
The User model is a part of Django's built-in models. This creates an authentication system and allows users to create accounts and make unique bookings.

The EventBooking model is a part of the bookings app and is for the user to create bookings. This is related to the Django built-in User model. It will create unique bookings for each user.

The ContactForm model is not related to any other model since it is not unique to any user. This model will save messages from users in the database but also send an email to both The Muscle Factory and an auto-reply to the user.

The Event model is for the admin to create events that will render on the landing page. This is to make it easy for the site owner to keep the website updated with relevant events. This is also related to the User model, but is for site owner and his/hers employees. 

![Database Models](docs/readme%20docs/images/db-models.png)


## Testing
### Code Validation
#### HTML
All html code has gone through Nu Html Checker. There were few errors. The errors came from Django's framework code. The errors have been documented and can be found inside registration.html and edit_item.html. Read more about these errors under Bugs section.

<details>
<summary>home.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2F
</details>

<details>
<summary>about.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fabout%2F
</details>

<details>
<summary>login.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Faccount%2Flogin%2F
</details>

<details>
<summary>logout.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Faccount%2Flogin%2F
</details>

<details>
<summary>registration.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Faccount%2Fsignup%2F
</details>

<details>
<summary>delete_booking.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fbookings%2Fmy_bookings%2Fdelete_booking%2Fe632fec1-63d7-4ba1-a429-0ec236cd98d8
</details>

<details>
<summary>edit_item.html</summary>
https://validator.w3.org/nu/?showsource=yes&useragent=Validator.nu%2FLV+http%3A%2F%2Fvalidator.w3.org%2Fservices&acceptlanguage=&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fbookings%2Fmy_bookings%2Fedit_item%2Fe632fec1-63d7-4ba1-a429-0ec236cd98d8%2F
</details>

<details>
<summary>my_bookings.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fbookings%2Fmy_bookings%2F#textarea
</details>

<details>
<summary>process_form.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fbookings%2Fprocess_form%2F#textarea
</details>

<details>
<summary>contact.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fcontact%2Fcontact%2F
</details>

<details>
<summary>error404.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2F404%2F#textarea
</details>


### CSS 
All CSS passed through validation and shows no errors:
<details>
<summary>style.css</summary>

![css](docs/readme%20docs/validation/css-validation/css-validation.png)
</details>

### JavaScript
All Javascript files has passed through validation and shows no errors:
<details>
<summary>script.js</summary>

![js](docs/readme%20docs/validation/js-validation/jshint.png)
</details>

### Python
<details>
<summary>Blog app</summary>

All Python files has passed through validation and shows no errors:
admin.py
![blog-admin](docs/readme%20docs/validation/python-linter-ci/blog-adminlinter.png)
views.py
![blog-views](docs/readme%20docs/validation/python-linter-ci/blog-viewslinter.png)
urls.py
![blog-urls](docs/readme%20docs/validation/python-linter-ci/blog-urlslinter.png)
models.py
![blog-models](docs/readme%20docs/validation/python-linter-ci/blogmodel-pylinter.png)
</details>

<details>
<summary>Bookings app</summary>

admin.py
![bookings-admin](docs/readme%20docs/validation/python-linter-ci/bookings-adminlinter.png)
view.py
![bookings-views](docs/readme%20docs/validation/python-linter-ci/bookings-viewslinter.png)
forms.py
![bookings-forms](docs/readme%20docs/validation/python-linter-ci/bookings-formlinter.png)
models.py
![bookings-models](docs/readme%20docs/validation/python-linter-ci/bookings-modelslinter.png)
urls.py
![bookings-urls](docs/readme%20docs/validation/python-linter-ci/bookings-urlslinter.png)
</details>

<details>
<summary>Contact app</summary>

admin.py
![contact-admin](docs/readme%20docs/validation/python-linter-ci/contact-adminlinter.png)
forms.py
![contact-forms](docs/readme%20docs/validation/python-linter-ci/contact-formslinter.png)
models.py
![contact-models](docs/readme%20docs/validation/python-linter-ci/contact-modellinter.png)
urls.py
![contact-urls](docs/readme%20docs/validation/python-linter-ci/contact-urlslinter.png)
view.py
![contact-views](docs/readme%20docs/validation/python-linter-ci/contact-viewslinter.png)
</details>

<details>
<summary>The Muscle Factory: main project</summary>

settings.py
![main-settings](docs/readme%20docs/validation/python-linter-ci/settings-pylinter.png)
urls.py
![main-urls](docs/readme%20docs/validation/python-linter-ci/the-muscle-factory-urlslinter.png)
</details>


### Testing User Stories
![userstories](docs/readme%20docs/ux-testing/userstorie-testing.png)

### Manuel Testing
Follow link to view manual testing:
[Click Me](docs/readme%20docs/README-TESTING.md)

### Lighthouse testing
![Lighthouse](docs/readme%20docs/images/lighthouse-testing.png)

### Browser Testing
The live webpage has been tested with:
- Mozilla
- Chrome
- Safari

No issues were found.

## Future Improvements
There are a lot of approvments I wish to do. This was a super fun project and I had to restrict myself to only create a MVP. 
Theese are some future improvments I wish to do:
- Add more styling to bookings pages
- Create new app to let members choose membership level
- Create better performance rate
- Create a function for admin to adjust information about services and employees
- I would like to change bookingform so only current time and forward of current day can be selected.

## Bugs
- Booking form not submitting:
The booking form will not submit when entering the booking link in the nav bar. It works fine if the form is entered from other link, like the ADD button from my bookings.
Status: Fixed

- Alignment issue:
There is an alignment issue unfixed, in edit_item, with "UPDATE" and "CANCEL" buttons. This is thought to have something to do with the form.as_p and Bootstrap classes. The buttons should be aligned.
Solution: No solution at the moment.

- The errors found with HTML validation checker: 
These errors are thought to occur because of the CSS styling to block the in form labels. The code passed trough validation comes from the live link of the webpage. From the code snippets used the labels are blocked. I think this is what is causing the problems, but since the code actually is there these are not really errors. The form is part of Django framework code which is why I can not just add a class or id to the labels. 
Solution: Remove CSS class display: block; before passing code through validation.


## Technologies used
### Libraries
- datetime
- uuid

### Languages
- Html
- CSS
- Python
- Javascript
- Django
- Bootstrap

### Packages
- psycop2: PostgreSQL
- dj3-cloudinary-storage
- Gunicorn
- Django
<details>
<summary>All Django-packages</summary>

![Django-framework](docs/readme%20docs/images/django-framework.png)
</details>

<details>
<summary>All packages</summary>

![Packages](docs/readme%20docs/images/packages.png)
</details>

### Framework and Websites
- Flake8: https://flake8.pycqa.org/en/latest/ 
To search for errors and unused libraries.
-  chatGPT: https://chat.openai.com/
For troubleshooting and writing text content.
- Pexels: https://www.pexels.com/sv-se/
To search for images.
- Google: https://www.google.com/webhp?hl=sv&sa=X&sqi=2&pjf=1&ved=0ahUKEwjD2YDFqvmDAxW_AhAIHcSrBckQPAgJ
To search for information.
- CSS validator: https://jigsaw.w3.org/css-validator/
Validate CSS.
- Html validator: https://validator.w3.org/
Validate HTML.
- Jshint: https://jshint.com/
Validate javascript.
- Code Institutes py linter: https://pep8ci.herokuapp.com/
Validate Python.
- Gitpod: https://gitpod.io/workspaces
API.
- GitHub: https://github.com/
Pushing all code and creating Kanban board.
- LucidChart: https://www.lucidchart.com/
For creating flowchart and database charts.
- Balsamiq: https://balsamiq.com/
To create all wireframes.
- Google Fonts: https://fonts.google.com/
To search for and borrow fonts.
- Font Awesome: https://fontawesome.com/
For borrowing font icons.
- Bootstrap: https://getbootstrap.com/ and https://getbootstrap.com/docs/5.3/getting-started/introduction/
To create classes.
- Favicon: https://favicon.io/
To create Kettlebell image - image was taken from google and then converted to favicon.
- Cloudinary: https://cloudinary.com/
For storing and editing image sizes.
- Google Excel: https://www.google.com/sheets/about/
To create sheets for documentation.
- Heroku: https://dashboard.heroku.com/
To deploy app.
- PostgreSQL
Database.
- EmailJS: https://www.emailjs.com/
Email function.
- Stack Overflow: https://stackoverflow.com/
Troubleshooting.
- W3Schools: https://www.w3schools.com/
Readin documentation.
- Youtube: https://www.youtube.com/
Link in footer and trouble shooting.
- Coolors: https://coolors.co/
To create a color chart.
- Am I responsive: https://ui.dev/amiresponsive
For testing wireframes.
- Code institute tutorials/ Walkthrough project
- Lighthouse testing
Creating a lighthouse report.
- Elephant SQL: https://customer.elephantsql.com/login
To handle the database.
- Perchance: https://perchance.org/ai-photo-generator?fbclid=IwAR2sOEfkPK5GW5uKOcfqvSraVwiDcZFSIkrOV8UP88daEPPKWJUa7ZwwuTo
Creating event post images.


## Deployment

### Create Heroku app
- Install Django and Gunicorn
- Install libraries: dj_database_url and psycopg2
- Install Cloudinary Libraries
- Create requirements.txt file
- Create a project with command django-admin startproject themusclefactory . (replace 
  themusclefactory with your project name). Do not forget the "." in the end, it's very important.
- Create app with command: python manage.py startapp blog (Replace 'blog' with name of your app)
- To create database models run: python manage.py makemigrations
- Then run: python manage.py migrate
### Before Deployment
- Set DEBUG=False in settings.py.
- Run pip3 freeze --local > requirements.txt .
- Remove env variable in Heroku settings: DISABLE_COLLECTSTATIC.
- Make sure that you have created a file called Procfile in project root. Start up
  command is inside Procfile and will inform Heroku how to run the app.
- Add your created apps in settings.py under INSTALLED_APPS.
- To run website you need to add allowed hosts under ALLOWED_HOSTS in settings.py. You    
  can find the host name if you try opening up the project with: python manage.py runserver.

### To deploy project in Heroku
- Create a Heroku account
- Log in to Heroku account
- In the dashboard choose "Create new app". It's located in the middle of the dashboard
- Give the new app a name and choose what region you are from
- When information is entered, find the tabs to Overview, Resources, Deploy, Metrics, Activity, Access and Settings. This should be in the upper right of the site. Click the "Settings" tab
- Find the Config Vars section and click the "Reveal Config Vars" Enter information if there is hidden information in the GitHub repository. In this project a creds.json file was entered. If you don't    
  have any hidden information in GitHub, step over the two following sections
- Inside Create config vars, enter KEYS and VALUE. Inside KEYS enter CREDS and copy and paste information from creds.json file, into VALUE. Click the "Add" button
- Add a new KEY with PORT and VALUE 8000. Click the "Add" button
- Scroll down to the Buildpacks section. Click the"Add buildpack" button
- Choose buildpack Python and "Save changes". Add another buildpack with nodjs. Save changes. It is important that the buildpacks are added in the correct order. Drag and drop buildpacks if they are in the wrong order
- When buildpacks are in order. Locate the "Deploy" tab. It's found on the left side of the "Settings" tab
- In the Deployment method section, choose GitHub to connect to the repository. Confirm request to connect to GitHub
- Search for the repo-name. This is the name of the repository. Click "Search"
- Click "Connect" to link Heroku app to GitHub repository
- Scroll down to Automatic deploy section and Manual deploy section
- Choose how the project should be deployed. If Enable Automatic Deploys, Heroku rebuilds the app every time new changes are pushed inside the working environment
- If Manual deploy is chosen the current state of the project will be deployed. For this alternative click "Deploy Branch".
- When the project is deployed there will be four green circles with check marks inside. There should be a message "Your app was successfully deployed.". Click the "View" button to see the deployed project. If steps are followed there should be a mock terminal with a project inside of it. Program starts automagically

### Fork repository in GitHub
- Log in to your GitHub account, or create a account if you don't have one
- Go to GitHub repository that you would like to fork. To
  find the repository, search for the repository URL inside the search bar
- At the top of the site in the right corner of the repository page there should be a button called "Fork". Click this button
- Choose where you would like to fork the repository
- GitHub will then create a clone of repository at chosen location. By default you should be directed to forked repository inside your gitHub account

## Credits
- I want to thank my fantastic mentor, Brian O'Hare, who always helps me with great feedback.
- I want to express my gratitude to my fiancé, who helped me proofread this fantastic README. He also tried to break my project several times, which helped me locate errors.
- I also want to extend my thanks to my colleagues on Slack. Thank you so much for taking the time to help me improve my project.
- Special thanks to Code Institute's tutor support, especially John, who helped me with some real headaches.
- This README was inspired by github user gStarHigh and 
- Last but not least, thank you to Code Institute for this truly enjoyable and informative project.