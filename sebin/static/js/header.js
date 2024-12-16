function closeHeader() {
    var header = document.getElementById("topHeader"); // ID가 올바른지 확인
    if (header) {
        header.style.display = "none"; // 헤더를 숨김
    } else {
        console.error("Element with ID 'topHeader' not found");
    }
}
