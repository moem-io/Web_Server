$(document).ready(function () {
    // $('.control_all_app_section').css('display', 'none');
    // $('.control_all_log_section').css('display', 'none');
    $('.control_all_node_section').css('display', 'none');

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
        // console.log('this.href', this.href);
        // console.log('url', url);
        return this.href == url || this.href + '/app' == url || this.href + '/log' == url || this.href + '/node' == url;
    }).addClass('active');


    $('.top_header .nav.menu .item').filter(function () {
        var url = window.location.href;
        // console.log('this.href', this.href);
        // console.log('url', url);
        var windowWidth = $(window).width();

        if (windowWidth < 960) {
            if (this.href + '/app' == url) {
                $('.control_all_app_section').css('display', 'block');
            } else if (this.href + '/log' == url) {
                $('.control_all_log_section').css('display', 'block');
            } else if (this.href + '/node' == url) {
                $('.control_all_node_section').css('display', 'block');
            }
        } else {
            $('.control_all_app_section').css('display', 'block');
            $('.control_all_log_section').css('display', 'block');
            $('.control_all_node_section').css('display', 'block');

        }
    });

    // var xmlText = localStorage.getItem("blockly.xml");
    // if (xmlText) {
    //     Blockly.mainWorkspace.clear();
    //     xmlDom = Blockly.Xml.textToDom(xmlText);
    //     Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, xmlDom);
    // }
    //
    // window.onunload = function () {
    //     if (event.clientX < 0 && event.clientY < 0) {
    //         alert("브라우저를 종료하였습니다.");
    //     }
    //
    // };



});

$(window).resize(function () {
    //창크기 변화 감지
    hide_else();
});

function hide_else() {
    $('.top_header .nav.menu .item').filter(function () {
        var url = window.location.href;
        // console.log('this.href', this.href);
        // console.log('url', url);
        var windowWidth = $(window).width();

        if (windowWidth < 960) {
            if (this.href + '/app' == url) {
                $('.control_all_log_section').css('display', 'none');
                $('.control_all_node_section').css('display', 'none');
            } else if (this.href + '/log' == url) {
                $('.control_all_app_section').css('display', 'none');
                $('.control_all_node_section').css('display', 'none');
            } else if (this.href + '/node' == url) {
                $('.control_all_app_section').css('display', 'none');
                $('.control_all_log_section').css('display', 'none');
            }
        } else {
            $('.control_all_app_section').css('display', 'block');
            $('.control_all_log_section').css('display', 'block');
            $('.control_all_node_section').css('display', 'block');

        }
    });

    // if (windowWidth < 960) {
//창 가로 크기가 500 미만일 경우
//         console.log("960");
    // $('.app_section.ui.segment').css('display','none');
    // $('.app_section.ui.segment').removeClass('segment');
    // $('.ui.centered.cards').css('margin-top', '60px', 'margin-bottom', '60px');

    // } else {
//창 가로 크기가 500보다 클 경우
//         console.log("200");
    // $('.app_section.ui').addClass('segment');
    // $('.ui.centered.cards').css('margin-top', '0px', 'margin-bottom', '0px');
    // }
}
