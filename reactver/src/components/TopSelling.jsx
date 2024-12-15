import FrameComponent1 from "./FrameComponent1";
import PropTypes from "prop-types";
import styles from "./TopSelling.module.css";

const TopSelling = ({ className = "" }) => {
  return (
    <div className={[styles.topSelling, className].join(" ")}>
      <div className={styles.topSellingTitle}>
        <h1 className={styles.topSelling1}>top selling</h1>
      </div>
      <div className={styles.topSellingProducts}>
        <div className={styles.topSellingFirstProduct}>
          <div className={styles.topSellingProductDetails}>
            <div className={styles.image7} />
          </div>
          <FrameComponent1
            frameDivFlex="unset"
            frameDivAlignSelf="stretch"
            secondStar="/star-2-4.svg"
            thirdStar="/star-3-4.svg"
            star5="/star-5-1.svg"
          />
        </div>
        <div className={styles.topSellingSecondProduct}>
          <div className={styles.topSellingSecondProductCon}>
            <div className={styles.topSellingSecondProductIma}>
              <div className={styles.imagePair}>
                <img
                  className={styles.image53Icon}
                  alt=""
                  src="/image-51@2x.png"
                />
              </div>
              <div className={styles.topSellingSecondProductNam}>
                <div className={styles.div}>레트로 후드집업</div>
                <div className={styles.topSellingSecondProductRat}>
                  <div className={styles.frameGroup}>
                    <div className={styles.starsPair}>
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-1.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-2-4.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-3-4.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-4-3.svg"
                      />
                      <img
                        className={styles.starsPairChild}
                        alt=""
                        src="/star-5-5.svg"
                      />
                    </div>
                    <div className={styles.productPricePairContainer}>
                      <span>4.5/</span>
                      <span className={styles.span}>5</span>
                    </div>
                  </div>
                  <div className={styles.topSellingSecondProductTry}>
                    <div className={styles.div1}>98,000원</div>
                    <div className={styles.viewAllButton}>
                      <div className={styles.virtualTryOn}>Virtual Try on</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className={styles.topSellingSecondProductIma}>
              <div className={styles.imagePair}>
                <div className={styles.image9} />
                <img
                  className={styles.imageIcon}
                  loading="lazy"
                  alt=""
                  src="/image@2x.png"
                />
              </div>
              <div className={styles.topSellingSecondProductNam}>
                <div className={styles.div2}>데님 홀터 드레스</div>
                <div className={styles.topSellingSecondProductRat}>
                  <div className={styles.frameGroup}>
                    <div className={styles.starParent}>
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-1.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-2-4.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-3-4.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-4-3.svg"
                      />
                      <img
                        className={styles.filledStarsPair}
                        alt=""
                        src="/star-5-4.svg"
                      />
                    </div>
                    <div className={styles.productPrice}>
                      <span>5.0/</span>
                      <span className={styles.span}>5</span>
                    </div>
                  </div>
                  <div className={styles.frameContainer}>
                    <div className={styles.wrapper}>
                      <div className={styles.div4}>82,000원</div>
                    </div>
                    <div className={styles.viewAllButton}>
                      <div className={styles.virtualTryOn}>Virtual Try on</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className={styles.viewAllButtonContainer}>
            <button className={styles.topSellingProductsContainer}>
              <a className={styles.viewAll}>View All</a>
            </button>
          </div>
        </div>
        <div className={styles.topSellingThirdProduct}>
          <div className={styles.imagePair}>
            <img className={styles.image8Icon} alt="" src="/image-8@2x.png" />
          </div>
          <div className={styles.topSellingSecondProductNam}>
            <div className={styles.div2}>스키니 핏 청바지</div>
            <div className={styles.topSellingThirdProductRati}>
              <div className={styles.frameGroup}>
                <div className={styles.starParent}>
                  <img
                    className={styles.filledStarsPair}
                    alt=""
                    src="/star-1.svg"
                  />
                  <img
                    className={styles.filledStarsPair}
                    alt=""
                    src="/star-2-4.svg"
                  />
                  <img
                    className={styles.filledStarsPair}
                    alt=""
                    src="/star-3-4.svg"
                  />
                  <img
                    className={styles.starsPairChild}
                    alt=""
                    src="/star-5-1.svg"
                  />
                </div>
                <div className={styles.productPrice}>
                  <span>3.5/</span>
                  <span className={styles.span}>5</span>
                </div>
              </div>
              <div className={styles.frameContainer}>
                <div className={styles.priceContainer}>
                  <div className={styles.div4}>39,000원</div>
                </div>
                <div className={styles.viewAllButton}>
                  <div className={styles.virtualTryOn}>Virtual Try on</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

TopSelling.propTypes = {
  className: PropTypes.string,
};

export default TopSelling;
