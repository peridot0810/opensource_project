import PropTypes from "prop-types";
import styles from "./BodyFirst.module.css";

const BodyFirst = ({ className = "" }) => {
  return (
    <div className={[styles.bodyFirst, className].join(" ")}>
      <div className={styles.mainImageFirstParent}>
        <div className={styles.mainImageFirst}>
          <div className={styles.mainImageSecond}>
            <img
              className={styles.vectorIcon}
              loading="lazy"
              alt=""
              src="/vector.svg"
            />
            <div className={styles.fitmeParent}>
              <h1 className={styles.fitme}>Fit.Me</h1>
              <div className={styles.imageDescription}>
                <h1 className={styles.h1}>
                  <p className={styles.p}>{`직접 입어보기 어렵다면? `}</p>
                  <p className={styles.p}>클릭 한번으로 착용해보기</p>
                </h1>
                <div className={styles.messageContainer}>
                  <div className={styles.fitmeConveysThe}>
                    "FitMe" conveys the message of "finding clothes that fit
                    me." It represents our goal of offering users an experience
                    where they can try on and find outfits that best suit their
                    body shape and style during the shopping process. We
                    emphasize the core value of personalized service, proposing
                    a customized shopping experience tailored to each customer.
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className={styles.shopButton}>
            <button className={styles.shopButtonItem}>
              <div className={styles.shopNow}>Shop Now</div>
            </button>
          </div>
        </div>
        <img className={styles.vectorIcon1} alt="" src="/vector-1.svg" />
      </div>
    </div>
  );
};

BodyFirst.propTypes = {
  className: PropTypes.string,
};

export default BodyFirst;
