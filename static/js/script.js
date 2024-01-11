
// Sets alert messages in contactform


const contactForm = document.getElementById('contactForm')

contactForm.addEventListener('submit', function(event) {
    event.preventDefault();
    sendMail(contactForm);
    //contactForm.submit();
});



//Send email with emailJS, then confirms successful or unsuccessful event, then resets the contactform if event is successful.
function sendMail(contactForm) {
    console.log('sendMail invoked');
    emailjs.send("service_ogoy0i8", "template_xb922ko", {
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
            }
        );  
        
}

