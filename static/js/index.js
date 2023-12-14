function sendMessage() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    //create an object to  store form data

    var formData = {
        name: name,
        email: email,
        message: message
    };

    //send a POST request to the server using AJAX

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit_contact_form', true) //replace with custom server endpoint
    xhr.setRequestHeader('Content-type', 'application/json');

    xhr.onload = function() {
        if (xhr.status === 200) {
            // Handle success
            alert ('Message sent successfully! Thank you for contacting us.');
        }else{
            //handle error
            alert ('Error sending messagge. Please try again later');
        }
    };

    // Convert the form data to json and send it to the server
    xhr.send(JSON.stringify(formData));
}
