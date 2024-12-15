import PasswordLabels from "../components/PasswordLabels";
import ExtraInfo from "../components/ExtraInfo";
import Button1 from "../components/Button1";
import styles from "./SignUp.module.css";

const SignUp = () => {
  return (
    <div className={styles.signUp}>
      <div className={styles.fitmeWrapper}>
        <a className={styles.fitme}>Fit.Me</a>
      </div>
      <div className={styles.koreanTitle}>
        <h1 className={styles.h1}>가입하기</h1>
      </div>
      <div className={styles.passwordInput}>
        <div className={styles.passwordFields}>
          <PasswordLabels />
        </div>
        <ExtraInfo />
      </div>
      <Button1
        button="Primary"
        buttonWidth="605px"
        buttonBackgroundColor="#000"
        buttonHeight="81px"
        viewAllProducts="회원 가입"
        viewAllProductsHeight="unset"
        viewAllProductsWidth="unset"
        viewAllProductsFontSize="36px"
        viewAllProductsDisplay="unset"
        viewAllProductsColor="#fff"
        viewAllProductsMargin="0"
      />
    </div>
  );
};

export default SignUp;
