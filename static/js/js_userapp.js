const slideMenu = function() {

    const navBlock = document.querySelector('#drop-menu');
    let toggleStatus = 1;

    const toggleMenu = function() {
        if (toggleStatus === 1) {
            document.querySelector('#hide-groups').style.display = 'none';
            toggleStatus = 0;
        } else if (toggleStatus === 0) {
            document.querySelector('#hide-groups').style.display = 'flex';
            toggleStatus = 1;
        }
    }

    navBlock.addEventListener('click', () => toggleMenu());

};

window.onload = function() {
    slideMenu();
};