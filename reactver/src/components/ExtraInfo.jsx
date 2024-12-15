import PropTypes from "prop-types";
import styles from "./ExtraInfo.module.css";

const ExtraInfo = ({ className = "" }) => {
  return (
    <div className={[styles.extraInfo, className].join(" ")}>
      <h3 className={styles.extraInformation}>Extra Information</h3>
      <div className={styles.uploadPhoto}>
        <div className={styles.div}>내 사진 업로드하기</div>
      </div>
      <div className={styles.photoContainerWrapper}>
        <div className={styles.photoContainer}>
          <div className={styles.photoContainerChild} />
          <img
            className={styles.image60Icon}
            loading="lazy"
            alt=""
            src="/image-60@2x.png"
          />
        </div>
      </div>
    </div>
  );
};

ExtraInfo.propTypes = {
  className: PropTypes.string,
};

export default ExtraInfo;
