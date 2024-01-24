### Manuel Testing
| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
|  Home/Landing  |                              |                                 | |   |
| Carousel       | Check time between slides |   Carousel is rotating in a 8 sec interval    |  8 seconds between sliding images |
| -Forward button | Click forward arrow | Takes the user to next slide | pass | Takes user to next slide |
| -backward button  | Click backward arrow | Takes user to prewius slide | Takes user to previous slide |
| "join us now" button | Click join us now | Takes user to registration form | Takes user to Registration form | 
| Responsivness | Make screen smaller than 768px | Text and button disappears on smaller screens | Text and join us now button disappears |

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
| Name field  | Try typing a name in name field| User can enter a name, field is required | Name is added |
| Lastname field  | Try tryping lastname | User can enter a name, field is not required | Lastname is added, lastname is not required |
| Phonenumber field | Try adding letters, try adding numbers| User can enter phonenumber, field is not required | Only letter e can be enterd, numbers can be enterd, field is not required|
| Email field    | Try not entering email adress, try enter email address | User can only enter email, field is required | User can only enter email Adress, is required | 
| Message | Try submiting form without message, try sending with message | User can enter text message, field is required | Form can not be submited without message, message is required |
| 'Submit' button | Click submit | Submits form | User receives email | 
| Alert message | Check alert | When form is submited there is a alers usccess message | Alert success displays |
| Email in admin panel | Sign in to admin panel, check contact forms | When form is submited the form is dislayed in admin panel | Message is received |
| Email The Muscle Factory | Check if form submited is in admin email | When form is submited The Muscle Factory receives a mail  | Email is received |
| Auto-reply | Check is user got an auto-reply when submiting form | The email enterd in the form gets an auto-reply after form is submitted | Auto-reply is received bu user | 

| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Bookings (not signed in) |       |  | 
| Bookings link  | Click Bookings button | Takes user to registration form | User is taken to register form | 


| Feature        |            Action           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Bookings (signed in)  |  |  | |
| Bookings link| Click bookings button  | Takes user to booking form | User is directed to bookings form | 
| Event date widget| Click event-date widget butotn | The widget shows only current date and future dates | User can view availabe dates |
| Start time widget| Click start time button | Time is selected between 08-17 | User can view times between 08-17 |
| Event select box|  Click Event-choice select box | Shows Personal trainer, Rehab, Massage and Dietist |  User can view Personal trainer, Rehab, Massage and Dietist |
| Options radio button| Try selecting multiple button, try not submittong | User can select one button | User can only enter one radio button | 
| Message field | Try sending form without message, try sending message | User can enter text message, is not required | If not message form is still submitted, if message, the information will show in submited form |
| 'Submit' button | Click button without entering any information in input fields, fill out form | Submits bookings form | Form is not submite, form is submited, redirects to my bookings | 
| Alert message| Check if there is an alert when form is submitted | When booking form is submitted, the user will have a alert success message | Alert displays | 
| Booking status |  | The booking is shown in  admin panel, and in My bookings  |


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| My Bookings |  |  | |
| Booking is for | Check | Shows name for user who created booking | Correct name | 
| Date| Check | Shows correct date for specified booking | Correct date | 
| Start time |  start time  | Shows correct time for specified booking | Correct start time
| Event choice|  check | Shows correct Event for specified booking | Correct event choice |
| Status| - | Shows is booking has been approved by admin |   -    |
| Your comment (if comment)| Check | If user has enterd a message it is displayed in specefied booking | Correct comment | 
| 'Edit' button | Click button | Takes user to edit booking page | Renders booking form with prefilled inputs with correct info |
| 'Delete' button|  Click delete button  | Takes user to delete booking page | Renders delete booking page | 
| 'Add' button| Click add button | Takes user to bookings form | Renders booking form | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Edit | |  | |
| Event date widget | Check info | Field should be occupied by previous information | Correct info is fetched | 
| Start time widget | Check | Field should be occupied by previous entered information | Correct info is fetched |
| Event choice | Check | Field should be occupied by previous entered information | Correct info is fetched |
| Options radio buttons | Check | Radio buttons should contain correct info | Correct info is fetched|
| Comment | Check| Comment should be fetched from previous made booking | Correct info is fetched | 
|'Update' button| Try updating form | Form updates | Form is updated |
|'Cancel' button | Click Cancel  | Redirects to my bookings, nothing is changed | Redirects My bookings | 
| Alert message |  Try updating form | Redirects My bookings, show alert | alert is displayed and user is redirected to my bookings | 
| Admin panel | Log in to admin panel, check bookings| Updated bookings should be updated | Bookings are updated | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Delete | |  | |
| Booking | Ceck | Correct booking is fetched | Correct booking is fetched | 
|'Delete' button|  Click delete button | Removes booking from my bookings | Booking is removed |
|'Return' button | Click return | Takes user back to my bookings without deleting booking | Redirect to My bookings |
| Alert message | Try deleting booking | If user deletes booking, there is a info alert message | Booking is deleted | 
| Admin panel | Check is deleted booking is removed from admin panel, booking | The deleted booking is removed from admin panel | Booking is deleted from admin panel | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Register |  |  | |
| Sign in link | Click sign in link | Takes user to sign in form | User is redirected to sign in form | 
| Username | Try not entering username: Enter user name | User can enter username | If no username user is adviced to add username: User name is added
| Password | Try not adding password: Try adding wrong password: Add correct password  | User can create a password | If no password user is adviced to enter password: If password is incorrect user is adviced to try different password: If Correct password user is signed in |
| Email| Try not adding email: Try adding allready existing email: Try adding email | User can enter email | If no email is enterd user can still create an account: Existing email, user is informed email adress is already in use: If new email is added a new account is created |
| 'Sign in' button | Click sign in button | User is signed in | User is signed in | 
| Alert message | Check when signing in | User will se a alert massage is signed in successfully | Alert message is displayed | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Sign in  |  | | |
| Register link | Click register link | Takes user to registration form |  | 
| Username field | Try entering username| User can enter username |n
| Password field | try entering wrong password: Enter correct password| User can enter password | |
| Alert message | Check when signing in | Signed in user will recieve alert message| pass | 
| 'Remember me' checkbox | Click remember me check box | When remember me is checked the user is rememberd | pass | 

| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Sign out  | |  | |
|'Sign out' button | Click sign out button| Signes user out | pass | 
|'Return' button | Click return | Takes user back to homepage |n
| Alert message | Ceck when signing out  | Signed out user will recieve Alert success message | pass | 


| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Navbar  |  |  | |
| 'Home' button |Click Home button| Takes user to homepage | pass | 
| 'About us' button |Click About us button | Takes user to About us |n |
| 'Contact us' button | Click Contact us button | Takes user to Contact us | pass | 
| 'Bookings' button (signed in) |Click bookings button | Takes user to registration form | pass | 
| 'Bookings' button (not signed in)| Click bookings button | Renders booking form |n
| 'My Bookings' button | Click My bookings button | Shows signed in user their booking | pass | 
| 'Sign in' button | Click Sign in button | Takes user to sign in form | pass | 
| 'Register' button | Click Register button| Takes user to registration, will disappear if user is signed in |n
| 'Sign out' button | Click Sign out button| Takes user to sign out page | pass | 
| 'Logo' button| Click logo | Logo takes user to homepage  | |
| Hamburger bar |check on smaller wireframes| Will appear on smaller wireframes | pass | 




| Feature        |            Acction           |             Expectation         |          Result           |
| -------------- |:----------------------------:| :------------------------------:| :-------------------------|
| Footer |  |  |  | 
| 'Facebook' link | Click Facebook link | Takes user to Facebook |n
| 'Instagram' link |Click Instagram link | Takes user to Instagram | pass | 
| 'Youtube' link | click Youtube link| Takes user to Youtube |n |






