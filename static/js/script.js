

var bootstrap_alert = function() {};

bootstrap_alert.error = function(message) {
    $('#alert_placeholder').html('<div class="alert alert-danger"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>');
}
bootstrap_alert.success = function(message) {
    $('#alert_placeholder').html('<div class="alert alert-success"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>');
}


    function sendMail(contactForm) {
        emailjs.send("service_supy7sf", "template_tgz8lrr", {
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
        return false;
    }
document.querySelector('.contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    sendMail(this);
});

/* Alert messages timeoutfunction */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);
