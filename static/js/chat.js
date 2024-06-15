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
        minute: "numeric"
    });
}

class AppMessageElement extends HTMLElement {
    constructor() {
        super();

        const date = new Date(Number(this.getAttribute("timestamp") || Date.now().toString()));
        const dateString = formatDate(date);

        this.innerHTML = `
            <div class="message-field">
                <span class="message-sender">${this.getAttribute("sender")}</span>
                <span class="message-content">${this.textContent}</span>
            </div>
            <div>
                <span class="message-timestamp">${dateString}</span>
            </div>
        `;
    }
}

window.customElements.define("app-message", AppMessageElement);