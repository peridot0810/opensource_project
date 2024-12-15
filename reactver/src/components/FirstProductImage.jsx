import { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./FirstProductImage.module.css";

const FirstProductImage = ({
  className = "",
  firstProductImageWidth,
  image54,
  image54IconHeight,
  prop,
  productStarFirstGap,
  productStarListAlignSelf,
  prop1,
  priceSeparatorDisplay,
  priceSeparatorMinWidth,
}) => {
  const firstProductImageStyle = useMemo(() => {
    return {
      width: firstProductImageWidth,
    };
  }, [firstProductImageWidth]);

  const image54IconStyle = useMemo(() => {
    return {
      height: image54IconHeight,
    };
  }, [image54IconHeight]);

  const productStarFirstStyle = useMemo(() => {
    return {
      gap: productStarFirstGap,
    };
  }, [productStarFirstGap]);

  const productStarListStyle = useMemo(() => {
    return {
      alignSelf: productStarListAlignSelf,
    };
  }, [productStarListAlignSelf]);

  const priceSeparatorStyle = useMemo(() => {
    return {
      display: priceSeparatorDisplay,
      minWidth: priceSeparatorMinWidth,
    };
  }, [priceSeparatorDisplay, priceSeparatorMinWidth]);

  return (
    <div
      className={[styles.firstProductImage, className].join(" ")}
      style={firstProductImageStyle}
    >
      <div className={styles.productImageContainer}>
        <img
          className={styles.image54Icon}
          loading="lazy"
          alt=""
          src={image54}
          style={image54IconStyle}
        />
      </div>
      <div className={styles.firstProductName}>
        <div className={styles.div}>{prop}</div>
        <div className={styles.productDetailFirst}>
          <div className={styles.productStar}>
            <div
              className={styles.productStarFirst}
              style={productStarFirstStyle}
            >
              <div className={styles.productStarSecond}>
                <div
                  className={styles.productStarList}
                  style={productStarListStyle}
                >
                  <img
                    className={styles.starOneIcon}
                    loading="lazy"
                    alt=""
                    src="/star-1.svg"
                  />
                  <img
                    className={styles.starOneIcon}
                    loading="lazy"
                    alt=""
                    src="/star-22.svg"
                  />
                  <img
                    className={styles.starOneIcon}
                    loading="lazy"
                    alt=""
                    src="/star-3-2.svg"
                  />
                  <img
                    className={styles.starOneIcon}
                    loading="lazy"
                    alt=""
                    src="/star-42.svg"
                  />
                  <img
                    className={styles.productStarListChild}
                    alt=""
                    src="/star-5-2.svg"
                  />
                </div>
                <div className={styles.div1}>{prop1}</div>
              </div>
              <div
                className={styles.priceSeparator}
                style={priceSeparatorStyle}
              >
                <span>4.5/</span>
                <span className={styles.span}>5</span>
              </div>
            </div>
          </div>
          <div className={styles.productVirtualTryon}>
            <div className={styles.virtualTryOn}>Virtual Try on</div>
          </div>
        </div>
      </div>
    </div>
  );
};

FirstProductImage.propTypes = {
  className: PropTypes.string,
  image54: PropTypes.string,
  prop: PropTypes.string,
  prop1: PropTypes.string,

  /** Style props */
  firstProductImageWidth: PropTypes.string,
  image54IconHeight: PropTypes.string,
  productStarFirstGap: PropTypes.string,
  productStarListAlignSelf: PropTypes.string,
  priceSeparatorDisplay: PropTypes.string,
  priceSeparatorMinWidth: PropTypes.string,
};

export default FirstProductImage;
