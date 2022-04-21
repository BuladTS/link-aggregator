const modalButtons = document.querySelectorAll('[data-modal-button]');
const modalClosebuttons = document.querySelectorAll('[data-modal-close]');
const allModals = document.querySelectorAll('[data-modal]');


modalButtons.forEach(function (item) {
    item.addEventListener('click', function () {
        const modalId = this.dataset.modalButton;
        const modal = document.querySelector('#' + modalId);
        modal.classList.remove('hidden');
        modal.querySelector('.modal-window').addEventListener('click', function (event) {
            event.stopPropagation();
        })
    })
})


modalClosebuttons.forEach(function (item) {
    item.addEventListener('click', function () {
        const modal = this.closest('[data-modal]');
        modal.classList.add('hidden');
    })
})


allModals.forEach(function (item) {
    item.addEventListener('click', function () {
        this.classList.add('hidden');
    })
})
