// Define our element references
const formSubmit = document.getElementById("submit");
const usernameBox = document.getElementById("username");
const passwordBox = document.getElementById("password");
const error = document.getElementById("error");

// Attach an event handler to the button
formSubmit.addEventListener("click", function() {
    const username = usernameBox.value;
    const password = passwordBox.value;

    if (username && password) {
        // Send an HTTP request via fetch
        fetch(new URL(location.href).pathname, {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": JSON.stringify({
                "username": username,
                "password": password // in a real application, the password is hashed before being sent across http
            })
        }).then(response => {
            if (response.redirected) {
                location.href = response.url;
            }
        });
    }
});

error.textContent = atob(new URL(window.location).searchParams.get("error") || "");