function handleUserIconClick() {
    // 사용자 상태에 따른 URL 리디렉션 처리
    var userStatus = "{{ user }}";
  
    if (userStatus === "Login_needed") {
      // 로그인되지 않은 경우 -> 로그인 페이지로 이동
      window.location.href = "{{ url_for('login') }}";
    } else if (userStatus === "root") {
      // 관리자 계정일 경우 -> 관리자 페이지로 이동
      window.location.href = "{{ url_for('user_manage') }}";
    } else {
      // 일반 유저일 경우 -> 마이페이지로 이동 (마이페이지 URL로 변경 필요)
      window.location.href = "{{ url_for('mypage') }}";
    }
  }