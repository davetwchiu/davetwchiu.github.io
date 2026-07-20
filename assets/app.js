(() => {
  const menuButton = document.querySelector('.menu-button');
  const nav = document.querySelector('.site-nav');
  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
    });
  }

  const buttons = document.querySelectorAll('.filter-button');
  const days = document.querySelectorAll('.day-section');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      buttons.forEach((item) => item.classList.toggle('active', item === button));
      days.forEach((day) => {
        day.hidden = filter !== 'all' && day.dataset.city !== filter;
      });
    });
  });
})();
