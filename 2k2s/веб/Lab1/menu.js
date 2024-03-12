const button = document.querySelector('button[aria-controls="mobile-menu"]');
const menu = document.querySelector('#mobile-menu');

button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true' || false;
    button.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('hidden');
});