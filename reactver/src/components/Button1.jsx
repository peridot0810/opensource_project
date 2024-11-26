import { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./Button1.module.css";

const Button1 = ({
  className = "",
  button = "Primary",
  buttonWidth,
  buttonBackgroundColor,
  buttonHeight,
  viewAllProducts,
  viewAllProductsHeight,
  viewAllProductsWidth,
  viewAllProductsFontSize,
  viewAllProductsDisplay,
  viewAllProductsColor,
  viewAllProductsMargin,
}) => {
  const buttonStyle = useMemo(() => {
    return {
      width: buttonWidth,
      backgroundColor: buttonBackgroundColor,
      height: buttonHeight,
    };
  }, [buttonWidth, buttonBackgroundColor, buttonHeight]);

  const viewAllProductsStyle = useMemo(() => {
    return {
      height: viewAllProductsHeight,
      width: viewAllProductsWidth,
      fontSize: viewAllProductsFontSize,
      display: viewAllProductsDisplay,
      color: viewAllProductsColor,
      margin: viewAllProductsMargin,
    };
  }, [
    viewAllProductsHeight,
    viewAllProductsWidth,
    viewAllProductsFontSize,
    viewAllProductsDisplay,
    viewAllProductsColor,
    viewAllProductsMargin,
  ]);

  return (
    <div
      className={[styles.button, className].join(" ")}
      data-button={button}
      style={buttonStyle}
    >
      <b className={styles.viewAllProducts} style={viewAllProductsStyle}>
        {viewAllProducts}
      </b>
    </div>
  );
};

Button1.propTypes = {
  className: PropTypes.string,
  viewAllProducts: PropTypes.string,

  /** Variant props */
  button: PropTypes.number,

  /** Style props */
  buttonWidth: PropTypes.string,
  buttonBackgroundColor: PropTypes.string,
  buttonHeight: PropTypes.string,
  viewAllProductsHeight: PropTypes.string,
  viewAllProductsWidth: PropTypes.string,
  viewAllProductsFontSize: PropTypes.string,
  viewAllProductsDisplay: PropTypes.string,
  viewAllProductsColor: PropTypes.string,
  viewAllProductsMargin: PropTypes.string,
};

export default Button1;
