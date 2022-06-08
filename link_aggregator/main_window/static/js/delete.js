const allFilesForDelete = document.querySelectorAll('[data-del-file]');
const allLinksForDelete = document.querySelectorAll('[data-del-link]');
let forms = document.querySelector('[data-del-form]').querySelectorAll('input');

forms[1].classList.add('hidden');
forms[2].classList.add('hidden');

function delClassAll() {
    allFilesForDelete.forEach(function (item) {
        item.classList.remove('marker_for_delete');
    })

    allLinksForDelete.forEach(function (item) {
        item.classList.remove('marker_for_delete');
    })
}


allFilesForDelete.forEach(function (item) {
    item.addEventListener('click', function () {
        delClassAll();
        item.classList.add('marker_for_delete');
        forms[1].setAttribute("value", 'file');
        forms[2].setAttribute("value",item.dataset.file);
    })
})

allLinksForDelete.forEach(function (item) {
    item.addEventListener('click', function () {
        delClassAll()
        item.classList.add('marker_for_delete');
        forms[1].setAttribute("value", 'link');
        forms[2].setAttribute("value", item.dataset.link);
    })
})