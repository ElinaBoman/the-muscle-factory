### Manuel Testing
| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
|  Home/Landing  |                              |                                 | |   |
| Carousel       |  |   Carousel is rotating in a 5 sec interval    |  
| -Forward button |  | Takes the user to next slide | pass ||
| -backward button  | | Takes user to prewius slide | |
| "join us now" button |  | Takes user to registration form | pass | 
| Responsivness | | Text and button disappears on smaller screens |n

| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
|  Event         |                              |                                 | |
| Pagination     | | If there are more then 3 events, they are paginated |       |

| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| About us       | |  |  | 
| Responsivness  | |  |n

| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Contact us  | | |  | 
| Name field  | | User can enter a name, field is required |n
| Lastname field  | | User can enter a name, field is not required | |
| Phonenumber field | | User can enter phonenumber, field is not required |       |
| Email field    |  | User can only enter email, field is required | pass | 
| Message | | User can enter text message, field is required |n
| 'Submit' button | | Submits form | pass | 
| Alert message | | When form is submited there is a alers usccess message |n
| Email in admin panel |  | When form is submited the form is dislayed in admin panel | |
| Email The Muscle Factory | | When form is submited The Muscle Factory receives a mail  |       |
| Auto-reply |  | The email enterd in the form gets an auto-reply after form is submitted | pass | 

| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Bookings (not signed in) |       |  | 
| Bookings link  |  | Takes user to registration form | pass | 


| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Bookings (signed in)  || | |
| Bookings link|   | Takes user to booking form | pass | 
| Event date widget|   | The widget shows only current date and future dates |n
| Start time widget| | Time is selected between 08-17 | |
| Event select box|   | Shows Personal trainer, Rehab, Massage and Dietist |       |
| Options radio button|  | User can select one button | pass | 
| Message field | are neat | User can enter text message, is not required |n
| 'Submit' button |  | Submits bookings form | pass | 
| Alert message|  | When booking form is submitted, the user will have a alert success message | pass | 
| Booking status | are neat | The booking is shown in  admin panel, and in My bookings  |n


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| My Bookings |  |  | |
| Booking is for | | Shows name for user who created booking | pass | 
| Date| | Shows correct date for specified booking | pass | 
| Start time |    | Shows correct time for specified booking |n
| Event choice|   | Shows correct Event for specified booking | |
| Status| | Shows is booking has been approved by admin |       |
| Your comment (if comment)|  | If user has enterd a message it is displayed in specefied booking | pass | 
| 'Edit' button | | Takes user to edit booking page |n |
| 'Delete' button|    | Takes user to delete booking page | pass | 
| 'Add' button| | Takes user to bookings form | pass | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Edit | |  | |
| Event date widget | centered          | Takes user to registration form | pass | 
| Start time widget | are neat   | Text and button disappears on smaller screens |n
| Event choice |                              |                                 | |
| Options radio buttons |             | Carousel is rotating in a 5 second interval |       |
| Comment | centered          | Takes the user to next slide | pass | 
|'Update' button| Takes user to prewius slide |n
|'Cancel' button | centered          | Takes user to registration form | pass | 
| Alert message | centered          | Takes the user to next slide | pass | 
| Admin panel | centered          | Takes the user to next slide | pass | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Delete | |  | |
| Booking |  | Correct booking is fetched | pass | 
|'Delete' button|   | Removes booking from my bookings |n
|'Return' button |  | Takes user back to my bookings without deleting booking | |
| Alert message |  | If user deletes booking, there is a info alert message | pass | 
| Admin panel |  | The deleted booking is removed from admin panel | pass | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Register |  |  |n |
| Sign in link |  | Takes user to sign in form | pass | 
| Username |  | User can enter username |n
| Password |   | User can create a password | |
| Alert message |  | User will se a alert massage is signed in successfully | pass | 
| 'Sign in' button | | User is signed in | pass | 

| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Sign in  |  | | |
| Register link | | Takes user to registration form |  | 
| Username field | | User can enter username |n
| Password field || User can enter password | |
| Alert message | | Signed in user will recieve alert message| pass | 
| 'Remember me' checkbox |  | When remember me is checked the user is rememberd | pass | 

| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Sign out  | |  | |
| 'Sign out' button | | Signes user out | pass | 
| 'Return' button | | Takes user back to homepage |n
| Alert message |  | Signed out user will recieve Alert success message | pass | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Navbar  |  |  | |
| 'Home' button | | Takes user to homepage | pass | 
| 'About us' button | | Takes user to About us |n |
| 'Contact us' button |  | Takes user to Contact us | pass | 
| 'Bookings' button (signed in) |  | Takes user to registration form | pass | 
| 'Bookings' button (not signed in)|  | Renders booking form |n
| 'My Bookings' button | | Shows signed in user their booking | pass | 
| 'Sign in' button | | Takes user to sign in form | pass | 
| 'Register' button | | Takes user to registration, will disappear if user is signed in |n
| 'Sign out' button | | Takes user to sign out page | pass | 
| 'Logo' button|  | Logo takes user to homepage  |n |
| Hamburger bar |  | Will appear on smaller wireframes | pass | 




| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Footer |  |  |  | 
| 'Facebook' link |    | Takes user to Facebook |n
| 'Instagram' link | | Takes user to Instagram | pass | 
| 'Youtube' link |   | Takes user to Youtube |n |






