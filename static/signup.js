document.getElementById('signForm').addEventListener('submit', function(event) {
    event.preventDefault()
    
    const username = document.getElementById('username').value
    const password = document.getElementById('password').value

    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username, password})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect
        } else {
            document.getElementById('message').textContent = data.message
        }
    })
    .catch(error => console.error('Error: ', error))
})