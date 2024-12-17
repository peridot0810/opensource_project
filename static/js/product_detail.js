document.querySelectorAll('.size-btn, .color-btn').forEach(button => {
    button.addEventListener('click', () => {
        // 모든 버튼에서 active 클래스 제거
        document.querySelectorAll('.size-btn, .color-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        // 클릭된 버튼에 active 클래스 추가
        button.classList.add('active');
    });
});


// 초기 수량 값
let quantity = 1;

// DOM 요소 가져오기
const quantityDisplay = document.getElementById("quantity");
const increaseBtn = document.getElementById("increase-btn");
const decreaseBtn = document.getElementById("decrease-btn");

// "+" 버튼 클릭 이벤트
increaseBtn.addEventListener("click", () => {
    quantity++;
    quantityDisplay.textContent = quantity; // 수량 업데이트
});

// "-" 버튼 클릭 이벤트
decreaseBtn.addEventListener("click", () => {
    if (quantity > 1) { // 수량이 1 이하로 내려가지 않게 설정
        quantity--;
        quantityDisplay.textContent = quantity;
    }
});