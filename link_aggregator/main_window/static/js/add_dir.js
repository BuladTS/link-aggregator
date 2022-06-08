const allDirs = document.querySelectorAll('[data-id-dir]');
const inputId = document.querySelector('#id_parent');
const inputListDate = document.querySelector('#id_dates');
const allFilesAddDir = document.querySelectorAll('[data-add-dir-file]');
const allLinksAddDir = document.querySelectorAll('[data-add-dir-link]');

let listDates = [0]; // Слева от нуля файлы а справа ссылки

inputListDate.classList.add('hidden');

function clearAll() {
    allDirs.forEach(function (item) {
        item.classList.remove('marker_for_delete');
    })
}

function updateDates() {
    inputListDate.textContent =`[${listDates}]`;
}

allDirs.forEach(function (item) {
    if (!item.classList.contains('label')) {
        item.addEventListener('click', function () {
            const id = item.getAttribute('data-id-dir');
            inputId.setAttribute("value", id);
            clearAll();
            item.classList.add('marker_for_delete');
        })
    }
})

allFilesAddDir.forEach(function (item) {
    item.addEventListener('click', function () {
        item.classList.toggle('marker_for_delete');
        if (item.classList.contains('marker_for_delete')) {
            listDates.unshift(parseInt(item.dataset.file));
            updateDates();
        } else {
            const firstIndex = listDates.indexOf(parseInt(item.dataset.file));
            listDates.splice(firstIndex,1);
            updateDates();
        }
    })
})

allLinksAddDir.forEach(function (item) {
    item.addEventListener('click', function () {
        item.classList.toggle('marker_for_delete');
        if (item.classList.contains('marker_for_delete')) {
            listDates.push(parseInt(item.dataset.link));
            updateDates();
        } else {
            const lastIndex = listDates.lastIndexOf(parseInt(item.dataset.link));
            listDates.splice(lastIndex, 1);
            updateDates();
        }
    })
})


