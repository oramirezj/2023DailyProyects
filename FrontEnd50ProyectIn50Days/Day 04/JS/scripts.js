/**** Bring data from DOM *****/
const search = document.querySelector('.search')
const btn = document.querySelector('.btn')
const input = document.querySelector('.input')

/******** Create a function to listen click and add class *****/
btn.addEventListener('click', () => {
    search.classList.toggle('active')
    input.focus()
})