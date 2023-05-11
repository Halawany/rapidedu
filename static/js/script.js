// Add event listener to navbar links to scroll to sections
const navLinks = document.querySelectorAll('.main-nav a');
navLinks.forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const targetId = link.getAttribute('href');
    const targetSection = document.querySelector(targetId);
    targetSection.scrollIntoView({ behavior: 'smooth' });
    const targetTitle = targetSection.querySelector('h2').innerText;
    document.title = targetTitle;
    window.history.pushState(null, null, targetId);
  });
});

// chatbot


// class Chatbox {
//   constructor() {
//       this.args = {
//           openButton: document.querySelector('.chatbox__button'),
//           chatBox: document.querySelector('.chatbox__support'),
//           sendButton: document.querySelector('.send__button')
//       }

//       this.state = false;
//       this.messages = [];
//   }

//   display() {
//       const {openButton, chatBox, sendButton} = this.args;

//       openButton.addEventListener('click', () => this.toggleState(chatBox))

//       sendButton.addEventListener('click', () => this.onSendButton(chatBox))

//       const node = chatBox.querySelector('input');
//       node.addEventListener("keyup", ({key}) => {
//           if (key === "Enter") {
//               this.onSendButton(chatBox)
//           }
//       })
//   }

//   toggleState(chatbox) {
//       this.state = !this.state;

//       // show or hides the box
//       if(this.state) {
//           chatbox.classList.add('chatbox--active')
//       } else {
//           chatbox.classList.remove('chatbox--active')
//       }
//   }

//   onSendButton(chatbox) {
//       var textField = chatbox.querySelector('input');
//       let text1 = textField.value
//       if (text1 === "") {
//           return;
//       }

//       let msg1 = { name: "User", message: text1 }
//       this.messages.push(msg1);

//       fetch('http://127.0.0.1:8000/', {
//           method: 'POST',
//           body: JSON.stringify({ message: text1 }),
//           mode: 'cors',
//           headers: {
//             'Content-Type': 'application/json'
//           },
//         })
//         .then(r => r.json())
//         .then(r => {
//           let msg2 = { name: "Sam", message: r.answer };
//           this.messages.push(msg2);
//           this.updateChatText(chatbox)
//           textField.value = ''

//       }).catch((error) => {
//           console.error('Error:', error);
//           this.updateChatText(chatbox)
//           textField.value = ''
//         });
//   }

//   updateChatText(chatbox) {
//       var html = '';
//       this.messages.slice().reverse().forEach(function(item, index) {
//           if (item.name === "Sam")
//           {
//               html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
//           }
//           else
//           {
//               html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
//           }
//         });

//       const chatmessage = chatbox.querySelector('.chatbox__messages');
//       chatmessage.innerHTML = html;
//   }
// }


// const chatbox = new Chatbox();
// chatbox.display();


$(document).ready(function() {
    
  $('#chatbot-icon').click(function() {
      openChatWindow();
  });

  $('#send-button').click(function() {
      sendMessage();
  });

  $('#message-input').keypress(function(event) {
      if (event.keyCode === 13) {
          sendMessage();
      }
  });


  $(window).scroll(function() {
      if ($(window).scrollTop() > 100) {
          $('#chatbot-icon').addClass('');
          closeChatWindow();
      } else {
          $('#chatbot-icon').removeClass('hidden');
      }
  });
});

function openChatWindow() {
  $('#chat-window').show();
  $('#message-input').focus();
}

function closeChatWindow() {
  $('#chat-window').hide();
}

function sendMessage() {
  const message = $('#message-input').val();
  if (message === '') {
      return;
  }
  $('#message-input').val('');
  const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
      method: 'POST',
      url: '/chatbot/',
      data: {
          message: message,
          csrfmiddlewaretoken: csrfToken
      },
      success: function(response) {
          const chatContainer = $('.chat-container');
          chatContainer.append('<div class="chat-message"><strong>You:</strong> ' + message + '</div>');
          chatContainer.append('<div class="chat-message"><strong>Chatbot:</strong> ' + response.response + '</div>');
          chatContainer.scrollTop(chatContainer.prop('scrollHeight'));
      },
      error: function(error) {
          console.error('Error:', error);
      }
  });
}

$(document).ready(function() {
    // Show the message element when the page loads
    $('#message').fadeIn();

    // Hide the message element and open the chat window when the chat icon is clicked
    $('#chatbot-icon').click(function() {
        $('#message').fadeOut();
        $('#chatbot-icon').addClass('hidden');
        openChatWindow();
    });
});