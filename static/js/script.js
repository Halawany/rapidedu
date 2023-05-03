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