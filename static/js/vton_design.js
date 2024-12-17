// 사용자 이미지 업로드 및 미리보기 기능
const userImageUploadInput = document.getElementById('user-image-upload');
const uploadedUserImage = document.getElementById('uploaded-user-image');

userImageUploadInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            uploadedUserImage.src = e.target.result; // 업로드한 사용자 이미지 미리보기
        }
        reader.readAsDataURL(file);
    }
});

// 상품 이미지 업로드 및 미리보기 기능
const productImageUploadInput = document.getElementById('product-image-upload');
const uploadedProductImage = document.getElementById('uploaded-product-image');

productImageUploadInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            uploadedProductImage.src = e.target.result; // 업로드한 상품 이미지 미리보기
        }
        reader.readAsDataURL(file);
    }
});
