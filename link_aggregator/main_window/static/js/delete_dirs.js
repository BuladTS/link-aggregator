const allDirsDel = document.querySelectorAll('[data-id-dir_del]');
const inputDelDirs = document.querySelector('#id_dirs')
let dirsDel = [];

inputDelDirs.classList.add('hidden');

function updateDate() {
    inputDelDirs.textContent = `[${dirsDel}]`
}

allDirsDel.forEach(function (item) {
    item.addEventListener('click', function () {
        item.classList.toggle('marker_for_delete');
        if (item.classList.contains('marker_for_delete')) {
            dirsDel.push(parseInt(item.getAttribute('data-id-dir_del')));
            updateDate()
        } else {
            const lastIndex = dirsDel.lastIndexOf(item.getAttribute('data-id-dir_del'))
            dirsDel.splice(lastIndex, 1);
            updateDate();
        }
    })
})


console.log(allDirsDel);