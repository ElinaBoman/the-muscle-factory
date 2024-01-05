
const emailSuccess = document.getElementById("email-success")

document.addEventListener("DOMContentLoaded", function() {
    const emailSuccess = document.getElementById("email-success");
    emailSuccess.classList.add("hide");
});


function sendMail(contactForm) {
    emailjs.send("service_supy7sf", "template_tgz8lrr", {
    "from_name": contactForm.name.value,
    "from_email": contactForm.email.value,
    "message": contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("Mail sent successfully:", response);
            contactForm.reset();
            emailSuccess.classList.remove('hide');
            setTimeout(function() {
                emailSuccess.classList.add('hide');
            }, 2000);   
        },
        function(error) {
            console.log("Error sending mail:", error);
        }
    );
    return false
}

