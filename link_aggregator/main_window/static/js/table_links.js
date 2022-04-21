const tableLinks = document.querySelectorAll('[data-links]');
const allDescriptions = document.querySelectorAll('[data-content]')


tableLinks.forEach(function (item) {
    item.addEventListener('click', function () {

        const description = document.querySelector('#' + this.dataset.link);
        
        allDescriptions.forEach(function (item) {
            item.classList.add('hidden');
        })
        description.classList.toggle('hidden');
    })
})


console.log(tableLinks);
console.log(allDescriptions);