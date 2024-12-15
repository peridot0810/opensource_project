import ButtonBase from "./ButtonBase";
import PropTypes from "prop-types";
import styles from "./Button.module.css";

const Button = ({
  className = "",
  destructive = false,
  hierarchy = "Primary",
  icon = false,
  size = "md",
  state = "Default",
}) => {
  return (
    <button
      className={[styles.button, className].join(" ")}
      data-destructive={destructive}
      data-hierarchy={hierarchy}
      data-icon={icon}
      data-size={size}
      data-state={state}
    >
      <ButtonBase icon="Leading" size="sm" />
    </button>
  );
};

Button.propTypes = {
  className: PropTypes.string,

  /** Variant props */
  destructive: PropTypes.bool,
  hierarchy: PropTypes.number,
  icon: PropTypes.number,
  size: PropTypes.number,
  state: PropTypes.number,
};

export default Button;
