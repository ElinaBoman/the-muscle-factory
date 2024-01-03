
function sendMail(contactForm) {

    emailjs.send("service_supy7sf", "template_tgz8lrr", {
    "from_name": contactForm.name.value,
    "from_email": contactForm.email.value,
    "message": contactForm.message.value
    });
    return;
};

 