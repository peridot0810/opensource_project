import LoginContainer from "../components/LoginContainer";
import styles from "./LogIn.module.css";

const LogIn = () => {
  return (
    <div className={styles.logIn}>
      <div className={styles.mainContainer}>
        <a className={styles.fitme}>Fit.Me</a>
      </div>
      <LoginContainer />
    </div>
  );
};

export default LogIn;
