// Define our element references
const formSubmit = document.getElementById("submit");
const usernameBox = document.getElementById("username");
const passwordBox = document.getElementById("password");

// Attach an event handler to the button
formSubmit.addEventListener("click", function() {
    const username = usernameBox.value;
    const password = passwordBox.value;

    if (username && password) {
        // Send an HTTP request via fetch
        fetch("/", {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "username": username,
                "password": password // in a real application, the password is hashed before being sent across http
            }
        });
    }
});