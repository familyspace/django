const slideMenu = function() {

    const navBlock = document.querySelector('#drop-menu');
    let toggleStatus = 0;

    const toggleMenu = function() {
        if (toggleStatus === 1) {
            document.querySelector('.hide-menu').style.display = 'none';
            toggleStatus = 0;
        } else if (toggleStatus === 0) {
            document.querySelector('.hide-menu').style.display = 'flex';
            toggleStatus = 1;
        }
    }

    navBlock.addEventListener('click', () => toggleMenu());

};

window.onload = function() {
    slideMenu();
};