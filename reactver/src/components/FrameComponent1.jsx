import { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./FrameComponent1.module.css";

const FrameComponent1 = ({
  className = "",
  frameDivFlex,
  frameDivAlignSelf,
  secondStar,
  thirdStar,
  star5,
}) => {
  const frameDivStyle = useMemo(() => {
    return {
      flex: frameDivFlex,
      alignSelf: frameDivAlignSelf,
    };
  }, [frameDivFlex, frameDivAlignSelf]);

  return (
    <div
      className={[styles.tParent, className].join(" ")}
      style={frameDivStyle}
    >
      <div className={styles.t}>롱 슬리브 펀칭 버튼 T</div>
      <div className={styles.productInfo}>
        <div className={styles.ratingContainer}>
          <div className={styles.starRow}>
            <img
              className={styles.firstStarIcon}
              loading="lazy"
              alt=""
              src="/star-1.svg"
            />
            <img
              className={styles.firstStarIcon}
              loading="lazy"
              alt=""
              src={secondStar}
            />
            <img
              className={styles.firstStarIcon}
              loading="lazy"
              alt=""
              src={thirdStar}
            />
            <img className={styles.starRowChild} alt="" src={star5} />
          </div>
          <div className={styles.emptyStar}>
            <span>3.5/</span>
            <span className={styles.span}>5</span>
          </div>
        </div>
        <div className={styles.parent}>
          <div className={styles.div}>39,000원</div>
          <div className={styles.virtualTryonContainer}>
            <div className={styles.virtualTryOn}>Virtual Try on</div>
          </div>
        </div>
      </div>
    </div>
  );
};

FrameComponent1.propTypes = {
  className: PropTypes.string,
  secondStar: PropTypes.string,
  thirdStar: PropTypes.string,
  star5: PropTypes.string,

  /** Style props */
  frameDivFlex: PropTypes.string,
  frameDivAlignSelf: PropTypes.string,
};

export default FrameComponent1;
