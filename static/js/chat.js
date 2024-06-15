const submit = document.getElementById("submit");
const messageInput = document.getElementById("message");
const messages = document.getElementById("messages");

/**
 * 
 * @param {Date} date 
 * @returns {string}
 */
function formatDate(date) {
    return date.toLocaleString("en-US", {
        weekday: "long",
        year: "numeric", 
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        hour12: true
    });
}

messageInput.addEventListener("keydown", function(event) {
    if (event.key == "Enter") {
        sendMessage();
    }
});

submit.addEventListener("click", function() {
    sendMessage();
});

function sendMessage() {
    if (messageInput.value) {
        const sender = "Test-Sender";
        const dateString = formatDate(new Date(Date.now()));
    
        const message = document.createElement("div");
        message.className = "app-message";
        message.setAttribute("sender", "Session-Test");
    
        message.innerHTML = `<div class="message-field">
                    <span class="message-sender">${sender}</span>
                    <span class="message-content">${messageInput.value}</span>
                </div>
                <div>
                    <span class="message-timestamp">${dateString}</span>
                </div>`;
    
        messages.prepend(message);
    
        // clear msg
        messageInput.value = "";
    }
}