const btnToggle = document.querySelector('.toggle-btn');
const table = document.querySelector('#table');

btnToggle.addEventListener('click', () => {
    document.getElementById('sidebar').classList.toggle('active');
    table.classList.toggle('col-10');
});

const navMenu = document.querySelector("#navMenu");

navMenu.addEventListener('click', () => {
    navMenu.classList.toggle("active");
})