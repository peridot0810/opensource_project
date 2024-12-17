document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("signup-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // 기본 제출 동작 방지

        // FormData 객체 생성
        const formData = new FormData();
        formData.append("product_name", document.getElementById("product_name").value);
        formData.append("product_explain", document.getElementById("product_explain").value);

        // 이미지 파일 추가
        const imageInput = document.getElementById("product_img");
        if (imageInput.files.length > 0) {
            formData.append("product_img", imageInput.files[0]);
        }

        try {
            // fetch를 이용한 POST 요청
            const response = await fetch("/signin_done", {
                method: "POST",
                body: formData // FormData 객체를 전송
            });

            const finalUrl = response.url;

            if (finalUrl.includes("/signin")) {
                alert(`회원가입 실패`);
                window.location.href = finalUrl;
            } else if (finalUrl.includes("/login")) {
                alert("회원가입 성공!");
                window.location.href = finalUrl;
            } else {
                alert("예상치 못한 응답입니다.");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("서버 오류가 발생했습니다. 다시 시도해주세요.");
        }
    });
});
