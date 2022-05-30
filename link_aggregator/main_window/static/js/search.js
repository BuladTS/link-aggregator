const searchLine = document.querySelector('[data-search]');
const filesAll = document.querySelectorAll('[data-files]');
const linksAll = document.querySelectorAll('[data-links]');



function hiddenAll() {
    filesAll.forEach(function (item) {
        item.classList.add('hidden');
    })
    linksAll.forEach(function (item) {
        item.classList.add('hidden');
    })
}

function showAll() {
    filesAll.forEach(function (item) {
        item.classList.remove('hidden');
    })
    linksAll.forEach(function (item) {
        item.classList.remove('hidden');
    })
}

searchLine.addEventListener('input', function () {
    let searchString = searchLine.value;
    if (searchString === '') {
        showAll();
    } else {
        hiddenAll();
    }

    filesAll.forEach(function (item) {
        let stringFile = item.querySelector('td');
        if (stringFile.textContent.includes(searchString)) {
            item.classList.remove('hidden');
        } else {
            let descriptionTagId = item.getAttribute('data-file');
            let description = document.querySelector('#description_files-' + descriptionTagId);
            let tag = document.querySelector('#tag_files-' + descriptionTagId);
            if (description.textContent.includes(searchString)) {
                item.classList.remove('hidden');
            }
            if (tag.textContent.includes(searchString)) {
                item.classList.remove('hidden');
            }
        }
    })
    linksAll.forEach(function (item) {
        let stringLink = item.querySelector('td');
        if (stringLink.textContent.includes(searchString)) {
            item.classList.remove('hidden');
        } else {
            let descriptionTagId = item.getAttribute('data-link');
            let description = document.querySelector('#description-' + descriptionTagId);
            let tag = document.querySelector('#tag-' + descriptionTagId);
            if (description.textContent.includes(searchString)) {
                item.classList.remove('hidden');
            }
            if (tag.textContent.includes(searchString)) {
                item.classList.remove('hidden');
            }
        }
    })

    if (searchString === '') {
        showAll();
    }
})
