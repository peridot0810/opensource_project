import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./FrameComponent.module.css";

const FrameComponent = ({ className = "", frame, frame1, frame2 }) => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/sign-up");
  }, [navigate]);

  const onTextClick1 = useCallback(() => {
    navigate("/log-in");
  }, [navigate]);

  return (
    <header className={[styles.frameParent, className].join(" ")}>
      <div className={styles.frameGroup}>
        <div className={styles.logInToTryOnAllOutfitsWrapper}>
          <div className={styles.logInTo}>Log in to try on all outfits.</div>
        </div>
        <img className={styles.frameIcon} loading="lazy" alt="" src={frame} />
      </div>
      <div className={styles.frameWrapper}>
        <div className={styles.headerParent}>
          <div className={styles.header}>
            <a className={styles.fitme}>Fit.Me</a>
            <div className={styles.navigation}>
              <div className={styles.shopParent}>
                <a className={styles.shop}>Shop</a>
                <img className={styles.frameIcon1} alt="" src={frame1} />
              </div>
            </div>
            <div className={styles.frameContainer}>
              <img className={styles.dividerIcon} alt="" src={frame2} />
              <input
                className={styles.searchForProducts}
                placeholder="Search for products..."
                type="text"
              />
            </div>
            <a className={styles.a}>{`고객센터 `}</a>
            <a className={styles.a1} onClick={onTextClick}>{`가입하기 `}</a>
            <a className={styles.a1} onClick={onTextClick1}>{`로그인 `}</a>
            <div className={styles.dividerParent}>
              <img className={styles.dividerIcon} alt="" src="/frame-3.svg" />
              <img className={styles.dividerIcon} alt="" src="/frame-4.svg" />
            </div>
          </div>
          <div className={styles.frameChild} />
        </div>
      </div>
    </header>
  );
};

FrameComponent.propTypes = {
  className: PropTypes.string,
  frame: PropTypes.string,
  frame1: PropTypes.string,
  frame2: PropTypes.string,
};

export default FrameComponent;
