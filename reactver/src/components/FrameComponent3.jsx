import PropTypes from "prop-types";
import styles from "./FrameComponent3.module.css";

const FrameComponent3 = ({ className = "" }) => {
  return (
    <div className={[styles.frameParent, className].join(" ")}>
      <img className={styles.frameIcon} alt="" src="/frame-61.svg" />
      <div className={styles.div}>
        <input className={styles.frame} type="checkbox" />
        <div className={styles.separator}>1</div>
        <img className={styles.frameIcon1} alt="" src="/frame-82.svg" />
      </div>
    </div>
  );
};

FrameComponent3.propTypes = {
  className: PropTypes.string,
};

export default FrameComponent3;
