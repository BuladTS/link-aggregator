const dropButtons = document.querySelectorAll('[data-drop]');

dropButtons.forEach(function (item) {
    item.addEventListener('click', function () {
        const dropSpanId = this.getAttribute('data-id');
        console.log(dropSpanId);
        const dropSpan = document.querySelector('#' + dropSpanId);
        console.log(dropSpan);
        dropSpan.classList.toggle('drop-flag');
        const dropContents = document.querySelectorAll('[data-dad]');
        dropContents.forEach(function (item) {
            if (item.dataset.dad === dropSpanId) {
                item.classList.toggle('hidden');
            }
        })
        console.log(dropContents);
    })
})
console.log(dropButtons);