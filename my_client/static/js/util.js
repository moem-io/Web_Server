$(document).ready(function () {
    $('.ui.sidebar').sidebar('attach events', '.ui.text.menu > nav.item > .hamburger.item');
    $('.ui.dropdown').dropdown();

    $('.footer .menu .item').removeClass('active');

    $('.footer .menu .item').filter(function () {
        var url = window.location.href;
        // console.log(this.href);
        return this.href == url;
    }).addClass('active');
});
