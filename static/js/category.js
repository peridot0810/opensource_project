/* 부모 컨테이너 스타일 */
.top-products-container {
    display: flex;
    justify-content: center; /* 요소들을 중앙에 배치 */
    align-items: flex-start; /* 세로 정렬 상단 맞춤 */
    flex-wrap: wrap; /* 화면이 줄어들면 요소를 다음 줄로 넘김 */
    gap: 20px; /* 각 상품 사이의 간격 */
    padding: 20px;
    max-width: 1440px; /* 최대 너비 설정 */
    margin: 0 auto; /* 화면 가운데 정렬 */
    margin-bottom: 50px;
    background-color: #ffffff;
}

/* 개별 상품 카드 스타일 */
.top-product {
    flex: 1 1 calc(33.333% - 40px); /* 3열 레이아웃 유지, 40px은 gap 보정 */
    max-width: calc(33.333% - 40px); /* 각 상품의 최대 너비 */
    background: #fff;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.2s;
}

.top-product:hover {
    transform: translateY(-5px);
}

/* 상품 이미지 */
.top-product-image {
    width: 100%;
    height: auto;
    border-radius: 10px;
    margin-bottom: 10px;
    object-fit: cover;
}

/* 상품 제목 */
.top-product-title {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* 평점 */
.top-product-rating {
    font-size: 14px;
    color: #ffcc00;
    margin-bottom: 10px;
}

/* 가격 */
.top-product-price {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Virtual Try On 버튼 */
.top-virtual-try-on {
    background-color: #52ffc0;
    border: none;
    color: #000;
    font-weight: bold;
    padding: 10px 15px;
    border-radius: 20px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.top-virtual-try-on:hover {
    background-color: #40d9a4;
}
