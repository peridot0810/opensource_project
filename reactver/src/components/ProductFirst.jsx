import FirstProductImage from "./FirstProductImage";
import PropTypes from "prop-types";
import styles from "./ProductFirst.module.css";

const ProductFirst = ({ className = "" }) => {
  return (
    <div className={[styles.productFirst, className].join(" ")}>
      <FirstProductImage
        image54="/image-54@2x.png"
        prop="베이직 롱 슬리브"
        prop1="38,000원"
      />
      <div className={styles.productSecond}>
        <div className={styles.secondProductImage}>
          <div className={styles.skinnyImage}>
            <div className={styles.image8Wrapper}>
              <img className={styles.image8Icon} alt="" src="/image-8@2x.png" />
            </div>
            <div className={styles.div}>스키니 핏 청바지</div>
            <div className={styles.skinnyDetail}>
              <div className={styles.productTwoRatingStarsParent}>
                <div className={styles.productTwoRatingStars}>
                  <img
                    className={styles.productTwoStars}
                    alt=""
                    src="/star-1.svg"
                  />
                  <img
                    className={styles.productTwoStars}
                    alt=""
                    src="/star-22.svg"
                  />
                  <img
                    className={styles.productTwoStars}
                    alt=""
                    src="/star-3-2.svg"
                  />
                  <img
                    className={styles.productTwoRatingStarsChild}
                    alt=""
                    src="/star-5-1.svg"
                  />
                </div>
                <div className={styles.productTwoRatingContainer}>
                  <span>3.5/</span>
                  <span className={styles.span}>5</span>
                </div>
              </div>
              <div className={styles.skinnyPriceNumberParent}>
                <div className={styles.skinnyPriceNumber}>
                  <div className={styles.div1}>39,000원</div>
                </div>
                <div className={styles.productTwoTryon}>
                  <div className={styles.virtualTryOn}>Virtual Try on</div>
                </div>
              </div>
            </div>
          </div>
          <div className={styles.productThird}>
            <img
              className={styles.productThirdChild}
              loading="lazy"
              alt=""
              src="/frame-34@2x.png"
            />
            <div className={styles.checkImage}>
              <div className={styles.div2}>체크 셔츠</div>
              <div className={styles.checkDetail}>
                <div className={styles.checkStar}>
                  <div className={styles.productThreeRatingStarsParent}>
                    <div className={styles.productThreeRatingStars}>
                      <img
                        className={styles.productTwoStars}
                        alt=""
                        src="/star-1.svg"
                      />
                      <img
                        className={styles.productTwoStars}
                        alt=""
                        src="/star-22.svg"
                      />
                      <img
                        className={styles.productTwoStars}
                        alt=""
                        src="/star-3-2.svg"
                      />
                      <img
                        className={styles.productTwoStars}
                        alt=""
                        src="/star-42.svg"
                      />
                      <img
                        className={styles.productTwoRatingStarsChild}
                        alt=""
                        src="/star-5-2.svg"
                      />
                    </div>
                    <div className={styles.div3}>18,000원</div>
                  </div>
                  <div className={styles.productThreeRatingContainer}>
                    <span>4.5/</span>
                    <span className={styles.span}>5</span>
                  </div>
                </div>
                <div className={styles.productThreeTryonContainerWrapper}>
                  <div className={styles.productThreeTryonContainer}>
                    <div className={styles.virtualTryOn}>Virtual Try on</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className={styles.viewMore}>
          <button className={styles.viewAllButtonContainer}>
            <a className={styles.viewAll}>View All</a>
          </button>
        </div>
      </div>
      <FirstProductImage
        firstProductImageWidth="295px"
        image54="/image-55@2x.png"
        image54IconHeight="349px"
        prop="베이지 버클 자켓"
        productStarFirstGap="1px"
        productStarListAlignSelf="unset"
        prop1="155,000원"
        priceSeparatorDisplay="unset"
        priceSeparatorMinWidth="unset"
      />
    </div>
  );
};

ProductFirst.propTypes = {
  className: PropTypes.string,
};

export default ProductFirst;
