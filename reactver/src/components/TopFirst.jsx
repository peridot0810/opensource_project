import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./TopFirst.module.css";

const TopFirst = ({ className = "" }) => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/sign-up");
  }, [navigate]);

  const onTextClick1 = useCallback(() => {
    navigate("/log-in");
  }, [navigate]);

  return (
    <header className={[styles.topFirst, className].join(" ")}>
      <div className={styles.tryonContainer}>
        <div className={styles.firstColumnSecond}>
          <div className={styles.logInTo}>Log in to try on all outfits.</div>
        </div>
        <img
          className={styles.frameIcon}
          loading="lazy"
          alt=""
          src="/frame1.svg"
        />
      </div>
      <div className={styles.secondColumn}>
        <div className={styles.loginContainer}>
          <a className={styles.fitme}>Fit.Me</a>
          <div className={styles.shopMenu}>
            <div className={styles.shopItem}>
              <a className={styles.shop}>Shop</a>
              <img className={styles.shopEmptyIcon} alt="" src="/frame-1.svg" />
            </div>
          </div>
          <div className={styles.searchMenu}>
            <img
              className={styles.searchEmptyIcon}
              alt=""
              src="/frame-22.svg"
            />
            <a className={styles.searchForProducts}>Search for products...</a>
          </div>
          <a className={styles.a}>{`고객센터 `}</a>
          <a className={styles.a1} onClick={onTextClick}>{`가입하기 `}</a>
          <a className={styles.a1} onClick={onTextClick1}>{`로그인 `}</a>
          <div className={styles.fitMeMenu}>
            <img className={styles.searchEmptyIcon} alt="" src="/frame-3.svg" />
            <img className={styles.searchEmptyIcon} alt="" src="/frame-4.svg" />
          </div>
        </div>
      </div>
    </header>
  );
};

TopFirst.propTypes = {
  className: PropTypes.string,
};

export default TopFirst;
