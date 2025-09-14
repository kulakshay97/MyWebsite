document.addEventListener('DOMContentLoaded', function(){
  const btn = document.getElementById('menu-btn');
  const nav = document.getElementById('nav');
  btn && btn.addEventListener('click', () => {
    nav.classList.toggle('show');
  });
});
