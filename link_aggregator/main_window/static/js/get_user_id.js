const id_block_link = document.querySelector('[data-id-user-link]');
const id_link = id_block_link.getAttribute('data-id-user-link');

const id_block_file = document.querySelector('[data-id-user-file]');
const id_file = id_block_file.getAttribute('data-id-user-file');


let form = document.querySelector('#id_user_link');

form.setAttribute("value", id_link);

let file = document.querySelector('#id_user_file');
console.log(file)
file.setAttribute("value", id_file);
