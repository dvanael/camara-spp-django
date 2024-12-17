document.addEventListener('keydown', function(event) {
  if (event.ctrlKey && event.key === 'p') {
    event.preventDefault();
    document.getElementById('id-search').focus();
  }
});