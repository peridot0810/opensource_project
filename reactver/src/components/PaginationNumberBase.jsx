import { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./PaginationNumberBase.module.css";

const PaginationNumberBase = ({
  className = "",
  shape = "Square",
  state = "Default",
  number,
  numberWidth,
}) => {
  const numberStyle = useMemo(() => {
    return {
      width: numberWidth,
    };
  }, [numberWidth]);

  return (
    <div
      className={[styles.root, className].join(" ")}
      data-shape={shape}
      data-state={state}
    >
      <div className={styles.content}>
        <div className={styles.number} style={numberStyle}>
          {number}
        </div>
      </div>
    </div>
  );
};

PaginationNumberBase.propTypes = {
  className: PropTypes.string,
  number: PropTypes.string,

  /** Variant props */
  shape: PropTypes.number,
  state: PropTypes.number,

  /** Style props */
  numberWidth: PropTypes.string,
};

export default PaginationNumberBase;
