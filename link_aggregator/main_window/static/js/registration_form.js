const inputs = document.querySelectorAll('input');

inputs.forEach(function (item,i) {
    if (i > 0) {
        item.classList.add('login');
    }
})

inputs[1].setAttribute("placeholder", "Login");
inputs[2].setAttribute("placeholder", "Password");
inputs[3].setAttribute("placeholder", "Repeat Password");