const btnToggle = document.querySelector('.toggle-btn');

btnToggle.addEventListener('click', () => {
    document.getElementById('sidebar').classList.toggle('active');
});

const navMenu = document.querySelector("#navMenu");

navMenu.addEventListener('click', () => {
    navMenu.classList.toggle("active");
})