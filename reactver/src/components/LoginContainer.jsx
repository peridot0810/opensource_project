import Button1 from "./Button1";
import PropTypes from "prop-types";
import styles from "./LoginContainer.module.css";

const LoginContainer = ({ className = "" }) => {
  return (
    <div className={[styles.loginContainer, className].join(" ")}>
      <div className={styles.credentialsContainer}>
        <h1 className={styles.h1}>로그인</h1>
        <div className={styles.div}>기존 회원이세요?</div>
      </div>
      <div className={styles.idContainer}>
        <div className={styles.div1}>아이디</div>
        <img className={styles.underlineIcon} alt="" src="/underline.svg" />
      </div>
      <div className={styles.passwordContainer}>
        <div className={styles.div2}>비밀번호</div>
        <div className={styles.passwordInput}>
          <img
            className={styles.underlineIcon1}
            loading="lazy"
            alt=""
            src="/underline.svg"
          />
        </div>
        <div className={styles.showPasswordContainer}>
          <div className={styles.showPasswordIcon} />
          <div className={styles.saveIdContainer}>
            <div className={styles.div3}>아이디저장</div>
          </div>
        </div>
      </div>
      <div className={styles.actionsContainer}>
        <Button1 button="Primary" viewAllProducts="기존 회원 로그인" />
        <div className={styles.footerLinks}>
          <div className={styles.div3}>아이디 찾기 | 비밀번호 찾기</div>
          <div className={styles.div5}>{`회원가입 `}</div>
        </div>
      </div>
    </div>
  );
};

LoginContainer.propTypes = {
  className: PropTypes.string,
};

export default LoginContainer;
