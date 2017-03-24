// 윈도우 창을 닫을 때 로그아웃 처리
function closePage(event) {
    if (event.clientY < 0) {
        // 로그아웃 처리
        console.log('logout')
        alert('logout')
    }

}

console.log('onkeydown');
document.onkeydown = function () {
    // 새로고침 방지 ( Ctrl+R, Ctrl+N, F5 )
    if (event.ctrlKey == true && ( event.keyCode == 78 || event.keyCode == 82 ) || event.keyCode == 116) {
        // event.keyCode = 0;
        // event.cancelBubble = true;
        // event.returnValue = false;
        alert('refresh')

    }


    // 창 닫기( Alt+F4 ) 방지
    if (event.keyCode == 115) { // F4 눌렀을 시
        // 로그아웃 처리
        alert('logout')

    }


    // 윈도우 창이 닫힐 경우
    if (event.keyCode == 505) {
        alert(document.body.onBeforeUnload);
    }
}