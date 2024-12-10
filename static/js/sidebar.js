const sidebar = document.querySelector('.sidebar');
const overlay = document.querySelector('.overlay');
const btnMenu = document.getElementById('open-sidebar');

btnMenu.addEventListener('click', () => {
  sidebar.classList.toggle('open');
  overlay.style.display = sidebar.classList.contains('open') ? 'block' : 'none';
});

overlay.addEventListener('click', () => {
  sidebar.classList.remove('open');
  overlay.style.display = 'none';
});


document.addEventListener('DOMContentLoaded', function () {
  if (window.innerWidth <= 576) {
    const navMenu = document.querySelector('.nav-menu');
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
      navMenu.appendChild(item.cloneNode(true));
    });
  }
});