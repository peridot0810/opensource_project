import PropTypes from "prop-types";
import styles from "./OutfitPreview.module.css";

const OutfitPreview = ({ className = "" }) => {
  return (
    <header className={[styles.outfitPreview, className].join(" ")}>
      <div className={styles.outfitPreview1}>
        <div className={styles.outfitPreview2}>
          <div className={styles.logInTo}>Log in to try on all outfits.</div>
        </div>
        <img
          className={styles.frameIcon}
          loading="lazy"
          alt=""
          src="/frame1.svg"
        />
      </div>
      <div className={styles.outfitPreview3}>
        <div className={styles.outfitPreview4}>
          <div className={styles.outfitPreview5}>
            <a className={styles.fitme}>Fit.Me</a>
            <div className={styles.navigation}>
              <div className={styles.shopLink}>
                <a className={styles.shop}>Shop</a>
                <img className={styles.frameIcon1} alt="" src="/frame-1.svg" />
              </div>
            </div>
            <div className={styles.search}>
              <img className={styles.frameIcon2} alt="" src="/frame-22.svg" />
              <input
                className={styles.searchForProducts}
                placeholder="Search for products..."
                type="text"
              />
            </div>
            <div className={styles.div}>{`고객센터 | 가입하기 | 로그인 `}</div>
            <div className={styles.language}>
              <img className={styles.frameIcon2} alt="" src="/frame-3.svg" />
              <img className={styles.frameIcon2} alt="" src="/frame-4.svg" />
            </div>
          </div>
          <div className={styles.outfitPreviewChild} />
        </div>
      </div>
    </header>
  );
};

OutfitPreview.propTypes = {
  className: PropTypes.string,
};

export default OutfitPreview;
