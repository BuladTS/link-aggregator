const tableLinks = document.querySelectorAll('[data-links]');
const allDescriptions = document.querySelectorAll('[data-content-description]');
const buttons = document.querySelectorAll('[data-pressed-button]');
const allTags = document.querySelectorAll('[data-content-tag]');
const allType = document.querySelectorAll('.link');

const tableFiles = document.querySelectorAll('[data-files]');
const allDescriptionsFiles = document.querySelectorAll('[data-content-description-files]');
const allTagsFiles = document.querySelectorAll('[data-content-tag-files]');

const tableFileNames = document.querySelectorAll('[data-cut-end]')

const downloadFile = document.querySelector('#download');

const shares = document.querySelectorAll('[data-share]')
const blockShare = document.querySelector('.social-contact');

if (allDescriptionsFiles.length === 0) {
    allDescriptions[0].classList.remove('hidden');
} else {
    allDescriptionsFiles[0].classList.remove('hidden');
}

blockShare.classList.add('hidden');

console.log(downloadFile)

buttons.forEach(function (item, i) {
    item.addEventListener('click', function () {
        buttons.forEach(function (item){
            item.classList.remove('pressed_button');
        })
        if (i === 0) {
            buttons[0].classList.toggle('pressed_button');
            allTags.forEach(function (item) {
                if (!item.classList.contains('hidden')) {
                     item.classList.add('hidden');
                     const description_id = item.getAttribute('data-description');
                     const description = document.querySelector('#' + description_id);
                     description.classList.toggle('hidden');
                 }
            })
            allTagsFiles.forEach(function (item) {
                if (!item.classList.contains('hidden')) {
                    item.classList.add('hidden');
                    const description_id = item.getAttribute('data-description');
                    const description = document.querySelector('#' + description_id);
                    description.classList.toggle('hidden');
                }
            })
        }
        else {
            buttons[1].classList.toggle('pressed_button');
            allDescriptions.forEach(function (item) {
                 if (!item.classList.contains('hidden')) {
                     item.classList.add('hidden');
                     const tag_id = item.getAttribute('data-tag');
                     const tag = document.querySelector('#' + tag_id);
                     tag.classList.toggle('hidden');
                 }
            })
            allDescriptionsFiles.forEach(function (item) {
                if (!item.classList.contains('hidden')) {
                    item.classList.add('hidden');
                    const tag_id = item.getAttribute('data-tag');
                    const tag = document.querySelector('#' + tag_id);
                    tag.classList.toggle('hidden');
                }

            })
        }

    })
})
console.log('1124');
tableLinks.forEach(function (item) {
    item.addEventListener('click', function () {
        if (buttons[0].classList.contains('pressed_button')) {
             const description = document.querySelector('#description-' + this.dataset.link);
             allDescriptions.forEach(function (item) {
                 item.classList.add('hidden');
             })
            allDescriptionsFiles.forEach(function (item) {
                item.classList.add('hidden');
            })
             description.classList.toggle('hidden');
        }
        else {
            const tag = document.querySelector('#tag-' + this.dataset.link);
            allTags.forEach(function (item) {
                item.classList.add('hidden');
            })
            allTagsFiles.forEach(function (item) {
                item.classList.add('hidden');
            })
            tag.classList.toggle('hidden');
        }
        blockShare.classList.remove('hidden');
        shares.forEach(function (i) {
            const link = item.querySelector('td').querySelector('span').textContent
            let href = i.getAttribute('href');
            href = href.slice(0, href.indexOf('=') + 1);
            i.setAttribute("href", href + link);
        })
        downloadFile.classList.add('hidden');
    })
})


tableFiles.forEach(function (item) {
    item.addEventListener('click', function () {
        if (buttons[0].classList.contains('pressed_button')) {
            const description = document.querySelector('#description_files-' + this.dataset.file);
            allDescriptionsFiles.forEach(function (item) {
                item.classList.add('hidden');
            })
            allDescriptions.forEach(function (item) {
                item.classList.add('hidden');
            })
            description.classList.toggle('hidden');
        }
        else {
            const tag = document.querySelector('#tag_files-' + item.dataset.file);
            allTags.forEach(function (item) {
                item.classList.add('hidden');
            })
            allTagsFiles.forEach(function (item) {
                item.classList.add('hidden');
            })
            tag.classList.toggle('hidden');
        }
        blockShare.classList.add('hidden');
        downloadFile.classList.remove('hidden');
        downloadFile.setAttribute("href", item.dataset.name);
    })
})


tableFileNames.forEach(function (item) {
    let string = item.textContent;
    const lastIndex = string.lastIndexOf('.');
    item.textContent = string.slice(0, lastIndex);
})


allType.forEach(function (item) {
    let string = item.textContent;
   const lastIndex = string.lastIndexOf('.');
    item.textContent = string.slice(lastIndex);
})
