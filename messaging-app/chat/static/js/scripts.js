// This file contains JavaScript code for client-side functionality, such as handling user interactions and updating the UI dynamically.

document.addEventListener('DOMContentLoaded', () => {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const messagesContainer = document.getElementById('messages-container');

    messageForm.onsubmit = (event) => {
        event.preventDefault();
        const message = messageInput.value;

        if (message) {
            sendMessage(message);
            messageInput.value = '';
        }
    };

    function sendMessage(message) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/send-message/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = () => {
            if (xhr.status === 200) {
                const newMessage = JSON.parse(xhr.responseText);
                displayMessage(newMessage);
            }
        };
        xhr.send(JSON.stringify({ message: message }));
    }

    function displayMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.innerText = message.content;
        messagesContainer.appendChild(messageElement);
    }
});