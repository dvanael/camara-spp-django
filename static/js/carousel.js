document.addEventListener('DOMContentLoaded', function () {
  const carouselList = document.querySelector('.carousel-list');
  const nextBtn = document.querySelector('.next-carousel');
  const prevBtn = document.querySelector('.prev-carousel');

  function scrollNext() {
    carouselList.scrollBy({
      left: carouselList.clientWidth,
      behavior: 'smooth'
    });
  }

  function scrollPrev() {
    carouselList.scrollBy({
      left: -carouselList.clientWidth,
      behavior: 'smooth'
    });
  }

  nextBtn.addEventListener('click', scrollNext);
  prevBtn.addEventListener('click', scrollPrev);
});

document.addEventListener('DOMContentLoaded', function () {
  const carouselList = document.querySelector('.vereadores-list');
  const nextBtn = document.getElementById('next-vereador');
  const prevBtn = document.getElementById('prev-vereador');

  function scrollNext() {
    carouselList.scrollBy({
      left: carouselList.clientWidth,
      behavior: 'smooth'
    });
  }

  function scrollPrev() {
    carouselList.scrollBy({
      left: -carouselList.clientWidth,
      behavior: 'smooth'
    });
  }

  nextBtn.addEventListener('click', scrollNext);
  prevBtn.addEventListener('click', scrollPrev);
});

// // Seleciona os carouséis
// const carouselVereadores = document.querySelector('.vereador-carousel');

// // Seleciona os botões de next e prev
// const nextVereador = document.getElementById('next-vereador');
// const prevVereador = document.getElementById('prev-vereador');

// // Função para ir para o próximo item do carousel
// function nextVereadorItem() {
//   const carouselList = carouselVereadores.querySelector('.vereadores-list');
//   const currentItem = carouselList.querySelector('.active');
//   const nextItem = currentItem.nextElementSibling;

//   if (nextItem) {
//     currentItem.classList.remove('active');
//     nextItem.classList.add('active');
//   }
// }

// // Função para ir para o item anterior do carousel
// function prevVereadorItem() {
//   const carouselList = carouselVereadores.querySelector('.vereadores-list');
//   const currentItem = carouselList.querySelector('.active');
//   const prevItem = currentItem.previousElementSibling;

//   if (prevItem) {
//     currentItem.classList.remove('active');
//     prevItem.classList.add('active');
//   }
// }

// // Adiciona eventos de clique aos botões de next e prev
// nextVereador.addEventListener('click', nextVereadorItem);
// prevVereador.addEventListener('click', prevVereadorItem);