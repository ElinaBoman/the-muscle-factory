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

![Am I resppnsive](./themusclefactory/docs/readme%20docs/air.png)

## Table of Contents
## UX
## Project Goals
## User Stories
## Flowchart
## General features
## Testing
## Code Validation
## Testing User Stories
## Manual Testing
## Future improvements
## Bugs
## Libraries and Software
## Final Result
## Deployment
## Github Pages
## Credits

## UX
The main goal for the website is to attract new members and also take care of members bookings. It was important that the website had a clean proffesional front. To make the website more interesting and also be able to show The Muscle Factorys matra a Bootstrap Carousel was placed on the landing page. The carousel shows images of the gym, members and some healty food to immideatly let the user know what the website is all about. The fist slide for example lets the user know that it's The Muscle Factorys misson to help members create a healthier lifestyle, but also how important it's to have a helpful community that supports members all the way.

### Colors and Fonts
To create a clean and proffessinal looking website calm colors were used. The main colors are gray but then there are some color pops to catch the eye of the user. This adds a bit of playfulness to the over all clinic looking front. Since this is a company that focus more on the longterm healt of members with not only gym membership but also massage, rehab and dietist it's more of a clinical gym and therefore the colors are more on the cool side. 

![Palette](./themusclefactory/docs/readme%20docs/colorpalette.png)


The fonts that are used are mainly clean and thin with dark colors. The headings are bold and thick creating a strong and sturdy look. The main text is balanced nicely with the thiner text creating a easy to read front. 
The font for heading has been borrowed from GoogleFonts, and the main text is set to the font of apple device's. 
* Heading: Bebas Neue, fallback: sans-serif
* Main text: apple-system, fallback: sans-serif

### Project Goals

The main goals for this project was:

* Create a website using Django Framework 

* Use: Bootstrap, python, javascript, CSS and HTML

* Create a website with full CRUD functionallity

* Creat a appeling frontend suiting a fitness website

* Use a database to store information about users and their appointments

* Set up email functionallity and use auto-reply

## User Stories
The Mucle Factory project was planned trough user stories. Theese stories were created from a user and site owner perspective. The stories describes what the project should include and would set the over all planing structure.

One importent part of this project was to use a agile development method. This would make the customers perspective very important but since this is not a real project with real customers, user stories were made up by creating potential customers and site owners. 

In agile development iterative and incremental development is a very important part. Each user storie represents a smaller and easier to manage part of the project. This helped a lot with planing the workload. 

As there was not a team bulding this project it might be hard to fully grasp the concept of agile development, since teamwork is a big part of that. Instead of having a team, I choose to create a chatgroup on Slack. Working with the critisim I got from fellow students, this turned out to be a very good idea. I got a lot of feedback that I later on implemented in my project, so big credits to my fiends on Slack. 

A Kanban board was created on GitHub to structure the project development. By taking all my user stories and labeling with their significanse for this project, it was a lot easier to assess each user storie after their relevance.

Not all user stories were finished, but all user stories with the label "MUST HAVE" were completed.

[Click to view Kanban board](https://github.com/users/ElinaBoman/projects/5/views/1)

![User Stories](./themusclefactory/docs/readme%20docs/UX.png)




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


## Flowchart

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

![Lucidchart](./themusclefactory/docs/readme%20docs/lucidchart.png)
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

Models connected to the database:

The User model is a part of Django's built-in models. This creates an authentication system and allows users to create accounts and make unique bookings.

The EventBooking model is a part of the bookings app and is for the user to create bookings. This is related to the Django built-in User model. It will create unique bookings for each user.

The ContactForm model is not related to any other model since it is not unique to any user. This model will save messages from users in the database but also send an email to both The Muscle Factory and an auto-reply to the user.

The Event model is for the admin to create events that will render on the landing page. This is to make it easy for the site owner to keep the website updated with relevant events. This is also related to the User model, but is for site owner and his/hers employees. 

![Database Models](./themusclefactory/docs/readme%20docs/db-models.png)

## General features

### Header and Navigation
The header and navigation menu is responsive and will change to suit different wireframes. On bigger screens the meny will display all navigation elemets, but on smaller screens the elements will be contained in a hamburger bar.
### Footer
### Register
### About us
### Contact us
### My bookings
- Edit
- Delete
- Add 
### Login
### Logout

## Libraries and Software

Lucidchart - https://www.lucidchart.com/

Coolors - https://coolors.co/