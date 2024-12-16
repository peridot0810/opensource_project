document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("signup-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // 기본 제출 동작 방지

        // 폼 데이터 가져오기
        const formData = {
            id: document.getElementById("id").value,
            pwd: document.getElementById("pwd").value,
            name: document.getElementById("name").value,
            phone: document.getElementById("phone").value,
            email: document.getElementById("email").value,
            type: document.querySelector('input[name="type"]:checked').value
        };

        try {
            // fetch를 이용한 POST 요청
            const response = await fetch("/signin_done", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            // 서버에서 리다이렉트를 보내기 때문에 response.url로 확인
            const finalUrl = response.url;

            if (finalUrl.includes("/login")) {
                // 성공 시 /login_userType으로 리다이렉트
                alert("회원가입 성공!");
                window.location.href = finalUrl; // 성공한 경로로 이동
            } else if (finalUrl.includes("/signin")) {
                // 실패 시 현재 페이지에 남아있고, flash 메시지가 있을 수 있으므로 flash 메시지를 확인
                const result = await response.text();
                alert(`회원가입 실패: ${result}`); // 서버가 보내는 flash 메시지를 출력
            } else {
                alert("예상치 못한 응답입니다.");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("서버 오류가 발생했습니다. 다시 시도해주세요.");
        }
    });
});
