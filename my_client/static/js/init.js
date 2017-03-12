$('#node').css("display", "none")


$('.meun.item').click(function () {
    //            alert('ho');
    if (!$(this).hasClass('active')) {
        $('.meun.item').removeClass('active')
    }
    $(this).addClass('active')
    //            alert($(this).text())

    if ($('.active').text() == "NODE") {
        //                alert($('.active').text())
        $('.card_section').css("display", "none");
        $('#node').css("display", "block");

    } else if ($('.active').text() == "APP") {
        $('.card_section').css("display", "block");
        $('#node').css("display", "none");

    } else {
        $('.card_section').css("display", "none");
        $('#node').css("display", "none");
    }
})


function card_detail() {
    var card_detail = document.getElementsByClassName("card_detail");
    var content_detail = document.getElementsByClassName("content_detail");
    var card_more_btn = document.getElementsByClassName("card_more_btn");

    //            card_detail[0].style.backgroundColor = "red";
    //            card_detail[0].style.height = "300px";

    if (card_more_btn[0].textContent == "more") {
        //                card_detail[0].style.backgroundColor = "red";
        card_detail[0].style.height = "300px";
        content_detail[0].style.display = "flex";
        card_more_btn[0].textContent = "less";
    } else {
        card_detail[0].style.height = "100px";
        content_detail[0].style.display = "none";
        card_more_btn[0].textContent = "more";

    }

}

function card_onoff() {
    var onoff = document.getElementsByClassName("card_onoff_btn");
    var card_detail = document.getElementsByClassName("card_detail");
    var card = document.getElementsByClassName("card");

    //            alert(onoff[0].textContent)
    if (onoff[0].textContent == "on") {
        onoff[0].textContent = "off";
        card_detail[0].style.background = "#ee3344";
        card[0].style.background = "#ee3344";

    } else {
        onoff[0].textContent = "on";
        card_detail[0].style.background = "#cccccc";
        card[0].style.background = "#cccccc";
    }
}