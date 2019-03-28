$(document).ready(function() {
	$(".drop-menu").click(function() {
		$(".flex-container-two").slideToggle(500);
	});
});

const slideMenu = function() {

    const navBlock = document.querySelector('#toggleMenu');
    let toggleStatus = 1;

    const toggleMenu = function() {
        if (toggleStatus === 1) {
            document.querySelector('.flex-container-wrapper').style.left = "-155px";
            toggleStatus = 0;
        } else if (toggleStatus === 0) {
            document.querySelector('.flex-container-wrapper').style.left = "0px";
            toggleStatus = 1;
        }
    }

    navBlock.addEventListener('click', () => toggleMenu());

};

window.onload = function() {
    slideMenu();
};