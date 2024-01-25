Table of Contents
# The Muscle Factory- A Django project, for Code Institute
# General 
The Muscle Factory is a website that lets users register for an account, book appointments and provieds information about upcomming events. The user can read about the services provided and the people working at The Muscle Factory. When the user has created and accont he/she can manage their bookings with full CRUD functionallity. This means that the user can: 
* Create a booking
* Rewiew their bookings
* Update and edit bookings
* Delete their bookings

The user will be kept up to date with upcoming events, that are manage by the admin panel. This is to always keep the website updated, and also attract new members with fun and creative events. 

The website is also equipped with a contact form where anyone can contact The Muscle Factory, this will also send a auto-reply to the user, to inform that their message has been sent and is awaiting a reply. 

The website is designed to make the user feel welcome regardless of their workout history. Everyone is welcome to join and form a new healty lifestyle with The Muscle Factory.

The idé for The Muscle Factory is based on my sisters personal trainer company. This project is only a simple example of what a fitness company website could look like and what features that are necessary. This project will hopefully be the base for my sisters company in the future.

Link to live website can be found here:
[Click Me](https://the-muscle-factory-9f171161969d.herokuapp.com/)

![Am I resppnsive](./themusclefactory/docs/readme%20docs/images/air.png)

### Project Goals

The main goals for this project was:

* Create a website using Django Framework 

* Use: Bootstrap, python, javascript, CSS and HTML

* Create a website with full CRUD functionallity

* Creat a appeling frontend suiting a fitness website

* Use a database to store information about users and their appointments

* Set up email functionallity and use auto-reply

## UX
The main goal for the website is to attract new members and also take care of members bookings. It was important that the website had a clean proffesional front. To make the website more interesting and also be able to show The Muscle Factorys matra a Bootstrap Carousel was placed on the landing page. The carousel shows images of the gym, members and some healty food to immideatly let the user know what the website is all about. The fist slide for example lets the user know that it's The Muscle Factorys misson to help members create a healthier lifestyle, but also how important it's to have a helpful community that supports members all the way.

### User Stories
The Mucle Factory project was planned trough user stories. Theese stories were created from a user and site owner perspective. The stories describes what the project should include and would set the over all planing structure.

One importent part of this project was to use a agile development method. This would make the customers perspective very important but since this is not a real project with real customers, user stories were made up by creating potential customers and site owners. 

In agile development iterative and incremental development is a very important part. Each user storie represents a smaller and easier to manage part of the project. This helped a lot with planing the workload. 

As there was not a team bulding this project it might be hard to fully grasp the concept of agile development, since teamwork is a big part of that. Instead of having a team, I choose to create a chatgroup on Slack. Working with the critisim I got from fellow students, this turned out to be a very good idea. I got a lot of feedback that I later on implemented in my project, so big credits to my fiends on Slack. 

A Kanban board was created on GitHub to structure the project development. By taking all my user stories and labeling with their significanse for this project, it was a lot easier to assess each user storie after their relevance.

Not all user stories were finished, but all user stories with the label "MUST HAVE" were completed.

[Click to view Kanban board](https://github.com/users/ElinaBoman/projects/5/views/1)

![User Stories](./themusclefactory/docs/readme%20docs/ux-testing/UX.png)


### User Stories Implementation
-  #2 As a user I can make bookings on the website so that I can plan my schedule
The user can create bookings and also view them on the website.

-  #3 As a user I can edit/delete bookings on the website so that I can change my schedule
There are options for the user to edit and delete their bookings.

-  #4 As a user I can create an account so I can see my bookings
There is a fully functioning authentication system so each user can view their own bookings and manage them.

-  #5 As a site owner I can create events so that I can display them on the website
In the admin panel the site owner can create events so that the website is allways up to date.

-  #6 As a site owner I can edit events so that I can display changes on the website
The site owner can manage the events, including changing published events.

-  #7 As a site owner I can get in contact with clients so that I can connect with clients
There is a contact form on the website collecting user information entered by the user. The user can, of course, choose if they want to display their full name and phone number; only the name and email are required. User informaiton is displayed in the admin panel.

-  #8 As a site owner I can delete events so that I can remove it from the website
The events can be deleted in the admin panel.

-  #9 As a user I can see available dates in a calendar so that I can schedule private sessions
The booking form will only show available dates and time in their widgets.

-  #10 As a site owner I can display pictures of the gym so I can attract more clients
This has not been fully completed. There is a picture of the gym in the Bootstrap carousel, but it's not clear enough that the image represents the gym. This would be a future implementation.

-  #11 As a site owner I can display and edit information about employees specialization so that I can attract more clients
This has not been completed. Even tough there is information about the employees, the admin does not have the abillity to change this information yet. This would me a future implementation. 

-  #12 As a user I can use the website on my phone so that I can make, edit and delete bookings with ease from my phone
The website is fully responsive and all booking features works on all viewports.

-  #13 As a site owner I can display information on the website so that I can inform clients about services and events
All services are described on the website.

### Colors and Fonts
To create a clean and proffessinal looking website calm colors were used. The main colors are gray but then there are some color pops to catch the eye of the user. This adds a bit of playfulness to the over all clinic looking front. Since this is a company that focus more on the longterm healt of members with not only gym membership but also massage, rehab and dietist it's more of a clinical gym and therefore the colors are more on the cool side. 

![Palette](./themusclefactory/docs/readme%20docs/images/colorpalette.png)


The fonts that are used are mainly clean and thin with dark colors. The headings are bold and thick creating a strong and sturdy look. The main text is balanced nicely with the thiner text creating a easy to read front. 
The font for heading has been borrowed from GoogleFonts, and the main text is set to the font of apple device's. 
* Heading: Bebas Neue, fallback: sans-serif
* Main text: apple-system, fallback: sans-serif


### Front End Structure
The Muscle Factory website is devided between if a user is authenticated or not. To view the full front end website the user must be registrerd and signed in. 

#### For a user who is not signed in following views avaialable are:
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

Registration button is exchanged with a greating to user.
- Contact Us
- About Us
- Bookings: 
When user is authenticated bookings view will allow user to enter a booking trough a form. To submit the form, the user needs to:
    
    - Choose service. The service provided are Personal trainer, Rehab, Massage or Dietist.
    - Choose time and date. The time and date widgets will only show avaialble dates and times. 
    - Enter if this is the users first appointment.
    - Extra comments, if there is anything the user would like to add, this field is not required.
- My Bookings

All bookings made by a user will be displayed, providing full CRUD functionality. If the user wants to delete a specific booking, the delete button will first render a view, asking if the user really wants to delete the booking. If the user deletes the booking, an alert will inform the user that the chosen booking has been deleted.
If the user would like to edit a booking, the booking form renders with prepopulated fields. If the user updated the booking there will be an alert informing user, that the booking has been updated.
If user wants to add a new booking from My Bookings view, the booking form will render.

- Logout

If signes out there is a alert message letting the user know if event was successfull. 


### Flowchart
To view project structure, see flowchart:
<details>
<summary>Lucidchart</summary>

![Lucidchart](./themusclefactory/docs/readme%20docs/images/lucidchart.png)
</details>


### Wireframes

To plan the design and responsivness of The Muscle Factory a tool called Balsamiq was used. This was in the early stages of the project and the images created dosn't represent the finished product. Balsamiq was used to visualize the project in diffrent wireframes.

See Balsamiq wireframes below:  

<details>
    <summary>Smaller devices</summary>

![Small](./themusclefactory/docs/readme%20docs/wireframes/wireframes-sm-landing-about-contact.png)

![Small](./themusclefactory/docs/readme%20docs/wireframes/wireframes-sm-create-delete.png)
</details>

<details>
  <summary>Medium devices</summary>

![Medium](./themusclefactory/docs/readme%20docs/wireframes/wireframes-md-landing-about.png)

![Medium](./themusclefactory/docs/readme%20docs/wireframes/wireframes-md-contact.png)

![Medium](./themusclefactory/docs/readme%20docs/wireframes/wireframes-md-create-bookings.png)
</details>
<details>
 <summary>Large devices</summary>

![Large](./themusclefactory/docs/readme%20docs/wireframes/wireframes-lg-landing.png)

![Large](./themusclefactory/docs/readme%20docs/wireframes/wireframes-lg-about.png)

![Large](./themusclefactory/docs/readme%20docs/wireframes/wireframes-lg-contacts.png)

![Large](./themusclefactory/docs/readme%20docs/wireframes/wireframes-lg-create.png)

![Large](./themusclefactory/docs/readme%20docs/wireframes/wireframes-lg-delete.png)

</details>

## Database

To store user information a relational database was used called PostgreSQL. The database is managed trough ElephantSQL. Read more about ElephantSQL in deployment section. 

#### The project contains four apps: User(AllAuth), Blog, Bookings and Contact.

The User model is a part of Django's built-in models. This creates an authentication system and allows users to create accounts and make unique bookings.

The EventBooking model is a part of the bookings app and is for the user to create bookings. This is related to the Django built-in User model. It will create unique bookings for each user.

The ContactForm model is not related to any other model since it is not unique to any user. This model will save messages from users in the database but also send an email to both The Muscle Factory and an auto-reply to the user.

The Event model is for the admin to create events that will render on the landing page. This is to make it easy for the site owner to keep the website updated with relevant events. This is also related to the User model, but is for site owner and his/hers employees. 

![Database Models](./themusclefactory/docs/readme%20docs/images/db-models.png)

## General features

### Header and Navigation
The header and navigation menu are responsive and will change to suit different wireframes. On bigger screens, the menu will display all navigation elements, but on smaller screens, the elements will be contained in a hamburger bar. The navbar also contains a kettlebell logo, same as in the title.
The navbar elements change depending on whether the user is signed in or not. For a user who is not signed in, the navigation elements are Home, About us, Contact us, and Booking. If the user is signed in, there will also be a link to My bookings.
![Header and Nav](./themusclefactory/docs/readme%20docs/images/features/header-navbar.png)
![Smaller nav](./themusclefactory/docs/readme%20docs/images/features/navbar-smaller.png)
![Nav bar collapsable](./themusclefactory/docs/readme%20docs/images/features/navbar.png)

### Home
The Home page is the landing page. This page contains a Bootstrap carousel with some pictures of the gym, members, and healthy food. This is to immediately describe the company to any user. The pictures are chosen because they resemble community and health. If the user is signed in, there will be a greeting displayed in the carousel. If a user is not signed in, there will instead be a 'Join us now' button that will take the user to the registration form. This is to have as few steps as possible between entering the website and getting users to sign up. The user does not need to look for the registration form since it's the first button on the landing page.

After the carousel, there is some informative text about the company and also the different memberships available.

The user can then read about upcoming events that are posted by the admin. Here fun and creative events are displayed. Not only describing training events but also social events since The Muscle Factory is all about creating a community with a supportive environment between members and employees. The events are clickable and will render more information about the event.

![Index](./themusclefactory/docs/readme%20docs/images/features/index-medals.png)
![Index](./themusclefactory/docs/readme%20docs/images/features/events-index.png)

### Footer
The footer has the same information on all pages. It contains opening hours, address, and links to social media. The footer is responsive and will change to fit different wireframes.
![Index](./themusclefactory/docs/readme%20docs/images/features/footer.png)

### Register
The Register/Sign up page collects Username, email address, and password. There is also a link to go directly to sign in, which will render the login form. There is information that describes criteria for selecting a password, making it easier for the user to create an account. The form is a part of Django's built-in allauth templates but has been styled to suit this project.
![Signup](./themusclefactory/docs/readme%20docs/images/features/signup.png)

### About us
The 'About Us' page briefly describes The Muscle Factory's services and employees. The main reason to have this page was to create a more personal connection to users. For a person who has never been to The Muscle Factory, it might seem scary to go to a new gym. In order to make new users feel more comfortable, the pictures of the employees show friendly faces. The description of services is made to make the user feel more secure and let them know that the services are personalized and unique to each user.
![About](./themusclefactory/docs/readme%20docs/images/features/aboutus.png)

### Contact us
The Contact Us page provides a form for any user to reach out. The form will be stored in the database where the admin can view them in Django's built-in Admin panel. The form will also send an email to The Muscle Factory's email account, and the user will receive an auto-reply. There is also an alert message informing the user of success or errors with the form. The fields collected are Name, Last name, Phone number, Email, and Message. The user can choose if they want to fill out the whole form. Only Name, Email, and Message are required.
![Database Models](./themusclefactory/docs/readme%20docs/images/features/contact-form.png)

### Bookings
If a user has not signed in, the Bookings link will instead take the user to the registration form. For a user who is signed in, there will be a form to create a booking. The form fields are Event date, Start time, Event choice. There is also a question if this is the user's first appointment. Lastly, the user can add information if there is anything they would like to add. The form will be saved to the database, where the admin can view bookings and approve appointments in the admin panel.
![Bookings](./themusclefactory/docs/readme%20docs/images/features/create-booking.png)

### My bookings
My bookings will be available to signed-in users. Here the user can view their bookings. The user can also choose to Edit, Delete, or Add their bookings.
![My bookings](./themusclefactory/docs/readme%20docs/images/features/)

### Login
If a user is registered, they can log in. This is a part of Django's built-in allauth forms. The user can choose to enter 'Remember me' to make future sign-ins easier. If the user does not have an account yet, there is a link to the registration form. When the user has successfully signed in, there will be an alert message.
![Login](./themusclefactory/docs/readme%20docs/images/features/signin.png)

### Logout
The logout page is for the user to sign out. Before a user can sign out, they have to confirm their action. If the user confirms that they want to sign out, the user will be logged out, and an alert message will confirm the action.
![Login](./themusclefactory/docs/readme%20docs/images/features/signout.png)


## Testing
### Code Validation
#### HTML
All html code has gone trough Nu Html Checker. There were few errors. The errors comes from Djangos framework code. The errors has been documented and can be found inside registration.html and edit_item.html.
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
<summary>event_detail.html</summary>
https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fthe-muscle-factory-9f171161969d.herokuapp.com%2Fthe-best-event-ever-known-to-man%2F
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
All CSS passed trough validation and shows no errors:
<details>
<summary>style.css</summary>

![css](./themusclefactory/docs/readme%20docs/validation/css-validation/css-validation.png)
</details>

### JavaScript
All Javascript files has passed through validation and shows no errors:
<details>
<summary>script.js</summary>

![js](./themusclefactory/docs/readme%20docs/validation/js-validation/jshint.png)
</details>

### Python
<details>
<summary>Blog app</summary>

All Python files has passed through validation and shows no errors:
admin.py
![blog-admin](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/blog-adminlinter.png)
views.py
![blog-views](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/blog-viewslinter.png)
urls.py
![blog-urls](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/blog-urlslinter.png)
models.py
![blog-models](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/blogmodel-pylinter.png)
</details>

<details>
<summary>Bookings app</summary>

admin.py
![bookings-admin](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/bookings-adminlinter.png)
view.py
![bookings-views](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/bookings-viewslinter.png)
forms.py
![bookings-forms](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/bookings-formlinter.png)
models.py
![bookings-models](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/bookings-modelslinter.png)
urls.py
![bookings-urls](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/bookings-urlslinter.png)
</details>

<details>
<summary>Contact app</summary>

admin.py
![contact-admin](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/contact-adminlinter.png)
forms.py
![contact-forms](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/contact-formslinter.png)
models.py
![contact-models](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/contact-modellinter.png)
urls.py
![contact-urls](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/contact-urlslinter.png)
view.py
![contact-views](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/contact-viewslinter.png)
</details>

<details>
<summary>The Muscle Factory: main project</summary>

settings.py
![main-settings](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/settings-pylinter.png)
urls.py
![main-urls](./themusclefactory/docs/readme%20docs/validation/python-linter-ci/the-muscle-factory-urlslinter.png)
</details>

### Testing User Stories
![userstories](./themusclefactory/docs/readme%20docs/ux-testing/userstorie-testing.png)
### Manuel Testing
[Click Me](/themusclefactory/docs/readme%20docs/README-TESTING.md)

### Lighthouse testing
![Lighthouse](/themusclefactory/docs/readme%20docs/images/lighthouse-testing.png)

## Future Improvments
## Bugs
## Libraries Languages and Software
## Deployment
### Fork repository
- Log in to your GitHub account, or create a account if you don't have one
- Go to GitHub repository that you would like to fork. To
find the repository, search for the repository URL inside the search bar
- At the top of the site in the right corner of repository page there should be a button called "Fork". Click this button
- Choose where you would like to fork the repository
- GitHub will then create a clone of repository at choosen location. By default you should be directed to forked repository inside your gitHub account
### To deploy project in Heroku
- Create a Heroku account
- Log in to Heroku account
- In the dashboard choose "Create new app". It's located in the middle of the dashboard
- Give the new app a name and choose what region you are from
- When information is entered, find the tabs to Overview, Resources, Deploy, Metrics, Activity, Access and Settings. This should be in the upper right of the site. Click the "Settings" tab
- Find the Config Vars section and click the "Reveal Config
Vars" Enter information if there is hidden information in the GitHub repository. In this project a creds.json file was entered. If you don't have any hidden information in GitHub, step over the two following sections
- Inside Create config vars, enter KEYS and VALUE. Inside KEYS enter CREDS and copy and paste information from creds.json file, into VALUE. Click the "Add" button
- Add a new KEY with PORT and VALUE 8000. Click the "Add" button
- Scroll down to the Buildpacks section. Click the"Add buildpack" button
- Choose buildpack Python and "Save changes". Add another buildpack with nodjs. Save changes. It is important that the buildpacks are added in the correct order. Drag and drop buildpacks if they are in the wrong order
- When buildpacks are in order. Locate the "Deploy" tab. It's found on the left side of the "Settings" tab
- In the Deployment method section, choose GitHub to connect to the repository. Confirm request to connect to GitHub
- Search for repo-name. This is the name of the repository. Click "Search"
- Click "Connect" to link Heroku app to GitHub repository
- Scroll down to Automatic deploy section and Manual deploy section
- Choose how the project should be deployed. If Enable Automatic Deploys, Heroku rebuilds the app every time new changes are pushed inside the working enviroment
- If Manual deploy is chosen the current state of the project will be deployed. For this alternative click "Deploy Branch".
- When the project is deployed there will be four green circles with checkmarks inside. There should be a message "Your app was successfully deployed.". Click the "View" button to see deployed project. If steps are followed there should be a mock terminal with project inside of it. Program starts automagically

## Credits

Lucidchart - https://www.lucidchart.com/

Coolors - https://coolors.co/