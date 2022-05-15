const id_block = document.querySelector('[data-id-user]');
const id = id_block.getAttribute('data-id-user');

let form = document.querySelector('#id_user');

form.setAttribute("value", id);
console.log(form)