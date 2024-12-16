document.addEventListener("DOMContentLoaded", () => {
    const loginButton = document.querySelector(".button");
    
    loginButton.addEventListener("click", async () => {
        const id = document.querySelector("input[placeholder='아이디 입력']").value;
        const pwd = document.querySelector("input[placeholder='비밀번호 입력']").value;
        const membershipType = document.querySelector("input[name='membership']:checked").value;

        if (!id || !pwd) {
            alert("아이디와 비밀번호를 입력해주세요.");
            return;
        }

        const requestData = {
            id: id,
            pwd: pwd,
            type: membershipType
        };

        try {
            const response = await fetch("/login_done", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(requestData)
            });

            const result = await response.json();

            if (response.ok) {
                // 로그인 성공 처리
                alert("로그인 성공!");
                window.location.href = "/home"; // 홈 페이지로 이동
            } else {
                // 로그인 실패 처리
                alert(result.message || "로그인에 실패했습니다.");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("서버와의 통신 중 문제가 발생했습니다.");
        }
    });
});
