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

$(window).resize(function () {
    //창크기 변화 감지
    open_chatroom();
});

function open_chatroom() {
    var windowWidth = $(window).width();
    if (windowWidth < 960) {
//창 가로 크기가 500 미만일 경우
        console.log("960");
        // $('.app_section.ui.segment').css('display','none');
        $('.app_section.ui.segment').removeClass('segment');
        $('.ui.centered.cards').css('margin-top', '60px', 'margin-bottom', '60px');

    } else {
//창 가로 크기가 500보다 클 경우
        console.log("200");

    }
}
