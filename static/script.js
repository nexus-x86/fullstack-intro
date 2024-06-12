document.getElementById('messageForm').addEventListener('submit',function(event) {
    event.preventDefault();
    const message = document.getElementById('message').value;
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `message=${message}`
    }).then(response=> {
        if (respond.status == 204) {
            const chatbox = document.getElementById('chatbox');
            const newMessage = document.createElement('div');
            newMessage.textContent = message;
            chatbox.appendChild(newMessage);
            document.getElementById('message').value='';
        }
    })
})