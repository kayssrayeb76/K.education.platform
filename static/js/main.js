// search icon click
let searchIcon = document.getElementById('search_icon');
let searchBox = document.getElementById('search_box');


searchIcon.addEventListener('click', (e) => {
    e.preventDefault();
    if (searchBox.style.width === '0px') {
        searchBox.style.width = '210px';
        searchBox.style.padding = '7.5px 10px';
        searchBox.style.border = '1px solid var(--secondary-color)';
        searchIcon.style.borderRightWidth = '0px';
        searchIcon.style.borderTopRightRadius = '0px';
        searchIcon.style.borderBottomRightRadius = '0px';
    } else {
        searchBox.style.width = '0px';
        searchBox.style.padding = '0px';
        searchBox.style.borderWidth = '0px';
        searchIcon.style.borderRightWidth = '1px';
        searchIcon.style.borderTopRightRadius = '8px';
        searchIcon.style.borderBottomRightRadius = '8px';
    }
});
