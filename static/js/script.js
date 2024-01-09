
// Sets alert messages in contactform
class bootstrap_alert {
    constructor() { }
    static success(message) {
        $('#alert_placeholder').html('<div class="alert alert-success"><a class="close" data-bs-dismiss="alert">×</a><span>' + message + '</span></div>');
    }
    static error(message) {
        $('#alert_placeholder').html('<div class="alert alert-danger"><a class="close" data-bs-dismiss="alert">×</a><span>' + message + '</span></div>');
    }
}

//Send email with emailJS, then confirms successful or unsuccessful event, then resets the contactform if event is successful.
function sendMail(contactForm) {
    emailjs.send("service_ogoy0i8", "template_xb922ko", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("Mail sent successfully:", response);
            bootstrap_alert.success('Mail sent succesfully!');
            contactForm.reset();
            },
    
        function(error) {
            console.log("Error sending mail:", error);
            bootstrap_alert.error('Mail was not sent');
            }
        );
    return false
}

