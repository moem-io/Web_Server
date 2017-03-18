$(document).ready(function () {
    $('.ui.sidebar').sidebar('attach events', '.ui.text.menu > nav.item > .hamburger.item');
    $('.ui.dropdown').dropdown();

    $('.control_footer .menu .item').removeClass('active');
    $('.control_footer .menu .item').filter(function () {
        var url = window.location.href;
        // console.log('this.href', this.href);
        // console.log('url', url);
        return this.href == url;
    }).addClass('active');

    $('.top_header .nav.menu .item').removeClass('active');
    $('.top_header .nav.menu .item').filter(function () {
        var url = window.location.href;
        // console.log('this.href', this.href);
        // console.log('url', url);
        return this.href == url || this.href + '/app' == url || this.href + '/log' == url || this.href + '/node' == url;
    }).addClass('active');

    $('.nav.sidebar.menu .item').removeClass('active');
    $('.nav.sidebar.menu .item').filter(function () {
        var url = window.location.href;
        console.log('this.href', this.href);
        console.log('url', url);
        return this.href == url || this.href + '/app' == url || this.href + '/log' == url || this.href + '/node' == url;
    }).addClass('active');

});
