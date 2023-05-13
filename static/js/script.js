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

// classroom

var links = document.querySelectorAll(".classroom-chapter-link");
var videoPlayer = document.querySelector("#classroom-video-player");

links.forEach(function(link) {
	link.addEventListener("click", function(event) {
		event.preventDefault();

		// Remove the active class from all chapter links
		links.forEach(function(link) {
			link.classList.remove("active");
		});

		// Add the active class to the clicked chapter link
		this.classList.add("active");

		// Get the video source URL from the clicked chapter link
		var videoUrl = this.getAttribute("data-video");

		// Set the video source and play the video
		videoPlayer.src = videoUrl;
		videoPlayer.play();
	});
});

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