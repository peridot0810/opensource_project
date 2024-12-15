import PropTypes from "prop-types";
import styles from "./ButtonBase.module.css";

const ButtonBase = ({ className = "", icon = "Leading", size = "md" }) => {
  return (
    <div
      className={[styles.buttonBase, className].join(" ")}
      data-icon={icon}
      data-size={size}
    >
      <img className={styles.arrowLeftIcon} alt="" src="/arrowleft.svg" />
      <div className={styles.text}>Previous</div>
    </div>
  );
};

ButtonBase.propTypes = {
  className: PropTypes.string,

  /** Variant props */
  icon: PropTypes.number,
  size: PropTypes.number,
};

export default ButtonBase;
