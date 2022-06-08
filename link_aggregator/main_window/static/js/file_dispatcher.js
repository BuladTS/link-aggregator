const dropButtons = document.querySelectorAll('[data-drop]');
const allFiles = document.querySelectorAll('[data-file]');
const allLinks = document.querySelectorAll('[data-link]');

const initialDirectories = document.querySelectorAll('.label');

dropButtons.forEach(function (item) {
    item.addEventListener('click', function () {
        const dropSpanId = this.getAttribute('data-id');
        const dropSpan = document.querySelector('#' + dropSpanId);
        dropSpan.classList.toggle('drop-flag');
        const dropContents = document.querySelectorAll('[data-dad]');
        dropContents.forEach(function (item) {
            if (item.dataset.dad === dropSpanId) {
                item.classList.toggle('hidden');
            }
        })
    })
})


function hiddenAll() {
    allFiles.forEach(function (item) {
        item.classList.add('hidden');
    })
    allLinks.forEach(function (item) {
        item.classList.add('hidden');
    })
}

function showFiles() {
    allFiles.forEach(function (item) {
        item.classList.remove('hidden');
    })
}

function showLinks () {
    allLinks.forEach(function (item) {
        item.classList.remove('hidden');
    })
}


initialDirectories.forEach(function (item) {
    item.addEventListener('click', function () {
        hiddenAll();
        const typeDate = this.dataset.type
        console.log(typeDate);
        if (typeDate === 'all') {
            showFiles();
            showLinks();
        }
        else if (typeDate === 'links') {
            showLinks();
        }
        else if (typeDate === 'files') {
            showFiles();
        } else {
            showFiles();
            showLinks();
        }

    })
})

