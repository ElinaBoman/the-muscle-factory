
// Constants
const contactForm = document.getElementById('contactForm')

/*
Eventlistener, prevents the email from being sent 
before completing the functions inside view.py. Then call sendMail
function.
*/
contactForm.addEventListener('submit', function(event) {
    event.preventDefault();
    sendMail(contactForm);
});


/* Send email with emailJS, then confirms successful or unsuccessful
event. If event is successfull the contactForm will execute submit().*/
function sendMail(contactForm) {
    
    emailjs.send("service_supy7sf", "template_tgz8lrr", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("Mail sent successfully:", response);
            contactForm.submit();
            },
    
        function(error) {
            console.log("Error sending mail:", error);
            return;
            }
        );      
}

