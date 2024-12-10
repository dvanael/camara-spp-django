const menu = document.querySelector('.nav-menu');
const menuBtn = document.querySelector('.btn-menu');

menuBtn.addEventListener('click', () => {
  menu.classList.toggle('d-none-mobile');
});