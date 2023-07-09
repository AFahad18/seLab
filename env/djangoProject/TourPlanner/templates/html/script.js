// WebSocket connection
const chatSocket = new WebSocket('ws://localhost:8000/ws/chat/room_name/');

// DOM elements
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatMessages = document.getElementById('chat-messages');

// Send button click event
sendButton.addEventListener('click', () => {
  const message = messageInput.value;
  if (message.trim() !== '') {
    sendMessage(message);
    messageInput.value = '';
  }
});

// Message input enter key event
messageInput.addEventListener('keydown', (event) => {
  if (event.keyCode === 13) {
    event.preventDefault();
    sendButton.click();
  }
});

// Send message function
function sendMessage(message) {
  const messageData = {
    message: message,
  };
  chatSocket.send(JSON.stringify(messageData));
}

// Receive message event
chatSocket.addEventListener('message', (event) => {
  const messageData = JSON.parse(event.data);
  const message = messageData.message;
  displayMessage(message);
});

// Display message function
function displayMessage(message) {
  const messageElement = document.createElement('div');
  messageElement.textContent = message;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}