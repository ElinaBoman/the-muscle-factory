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

In agile development iterative and incremental development is a very important part. So by adressing user stories the development of building The Muscle Factory could be split into smalller and easier to manage segments that could be iterated and improved by each iteration. 

As there was not a team bulding this project it might be hard to fully grasp the concept of agile development, since teamwork is a big part of that. Instead of having a team, I choose to create a chatgroup on Slack. Working with the critisim I got from fellow students, this turned out to be a very good idea. I got a lot of feedback that I later on implemented in my project, so big credits to my fiends on Slack. 

A Kanban board was created on GitHub to structure the project development. By taking all my user stories and labeling with their significanse for this project, it was a lot easier to assess each user storie after their relevance.

Not all user stories were finished, but they all user stories with the label "MUST HAVE" were completed.


![User Stories](./themusclefactory/docs/readme%20docs/UX.png)

[Click to view Kanban board](https://github.com/users/ElinaBoman/projects/5/views/1)

### #2 As a user I can make bookings on the website so that I can plan my schedule
The user can create bookings and also view them on the website. 


### #3 As a user I can edit/delete bookings on the website so that I can change my schedule
There are options for the user to edit and delete their bookings.

### #4 As a user I can create an account so I can see my bookings
There is a fully functioning authentication system so each user can view their own bookings and manage them. 

### #5 As a site owner I can create events so that I can display them on the website
In the admin panel the site owner can create events so that the website is allways up to date.

### #6 As a site owner I can edit events so that I can display changes on the website
The site owner can manage the events, including changing published events.

### #7 As a site owner I can get in contact with clients so that I can connect with clients
There is a contact form on the website collecting user information entered by the user. The user can, of course, choose if they want to display their full name and phone number; only the name and email are required. User informaiton is displayed in the admin panel.

### #8 As a site owner I can delete events so that I can remove it from the website
The events can be deleted in the admin panel.

### #9 As a user I can see available dates in a calendar so that I can schedule private sessions
The booking form will only show available dates and time in their widgets.

### #10 As a site owner I can display pictures of the gym so I can attract more clients
This has not been fully completed. There is a picture of the gym in the Bootstrap carousel, but it's not clear enough that the image represents the gym. This would be a future implementation.

### #11 As a site owner I can display and edit information about employees specialization so that I can attract more clients
This has not been completed. Even tough there is information about the employees, the admin does not have the abillity to change this information yet. This would me a future implementation. 

### #12 As a user I can use the website on my phone so that I can make, edit and delete bookings with ease from my phone
The website is fully responsive and all booking features works on all viewports.

### #13 As a site owner I can display information on the website so that I can inform clients about services and events
All services are described on the website.






![User Stories](./themusclefactory/docs/readme%20docs/lucidchart.png)
## Libraries and Software

Lucidchart - https://www.lucidchart.com/
