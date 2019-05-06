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

$(document).ready(function(){
    $('.taskcheckbox').on('change', function (event) {
        console.log('Привет');
        var target_href = event.target;
        if (target_href) {
            $.ajax({
                url: "checkbox/" + target_href.name + "/",
                success: function (data) {
                    $('.taskcheckbox').html(data.result);

                },
                complete: function() {
                    window.location.reload();
                },
            });
        }
        event.preventDefault();
    });
});


window.onload = function() {
    slideMenu();
};