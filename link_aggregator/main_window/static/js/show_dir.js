const userDirs = document.querySelectorAll('[data-id-dirs]')

userDirs.forEach(function (item) {
    item.addEventListener('click', function() {
        const idDir = item.getAttribute('data-id-dirs');
        checkHaveIdDir(Number(idDir));
    })
})


function checkHaveIdDir(id) {
    tableLinks.forEach(function (item) {
        let listWithId = item.getAttribute('data-dirs');
        listWithId = JSON.parse(listWithId);
        if (listWithId.includes(id)) {
            item.classList.remove('hidden');
        } else {
            item.classList.add('hidden');
        }
    })

    tableFiles.forEach(function (item) {
        let listWithId = item.getAttribute('data-dirs');
        listWithId = JSON.parse(listWithId);
        if (listWithId.includes(id)) {
            console.log('12')
            item.classList.remove('hidden');
        } else {
            item.classList.add('hidden');
        }
    })
}
