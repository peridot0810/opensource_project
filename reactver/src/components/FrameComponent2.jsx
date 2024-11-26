import PropTypes from "prop-types";
import styles from "./FrameComponent2.module.css";

const FrameComponent2 = ({ className = "" }) => {
  return (
    <div className={[styles.frameWrapper, className].join(" ")}>
      <div className={styles.frameParent}>
        <div className={styles.frameContainer}>
          <div className={styles.breadcrumbLinksParent}>
            <div className={styles.breadcrumbLinks}>
              <div className={styles.frameGroup}>
                <div className={styles.homeWrapper}>
                  <a className={styles.home}>Home</a>
                </div>
                <img
                  className={styles.outerLinkIcon}
                  alt=""
                  src="/frame-6@2x.png"
                />
              </div>
            </div>
            <div className={styles.breadcrumbLinks}>
              <div className={styles.frameGroup}>
                <div className={styles.homeWrapper}>
                  <div className={styles.shop}>Shop</div>
                </div>
                <img
                  className={styles.outerLinkIcon}
                  alt=""
                  src="/frame-6@2x.png"
                />
              </div>
            </div>
            <div className={styles.breadcrumbLinks}>
              <div className={styles.frameGroup}>
                <div className={styles.homeWrapper}>
                  <a className={styles.women}>Women</a>
                </div>
                <img
                  className={styles.outerLinkIcon}
                  alt=""
                  src="/frame-6@2x.png"
                />
              </div>
            </div>
            <div className={styles.outers}>Outers</div>
          </div>
        </div>
        <div className={styles.frameParent2}>
          <div className={styles.frameWrapper1}>
            <div className={styles.image64Parent}>
              <img
                className={styles.image64Icon}
                loading="lazy"
                alt=""
                src="/image-64@2x.png"
              />
              <img
                className={styles.image64Icon}
                loading="lazy"
                alt=""
                src="/image-66@2x.png"
              />
            </div>
          </div>
          <div className={styles.image51Wrapper}>
            <img
              className={styles.image51Icon}
              loading="lazy"
              alt=""
              src="/image-511@2x.png"
            />
          </div>
          <div className={styles.frameWrapper2}>
            <div className={styles.frameParent3}>
              <div className={styles.frameParent4}>
                <div className={styles.frameWrapper3}>
                  <div className={styles.parent}>
                    <h1 className={styles.h1}>레트로 후드집업</h1>
                    <div className={styles.frameParent5}>
                      <div className={styles.starsParent}>
                        <div className={styles.stars}>
                          <img
                            className={styles.starsChild}
                            loading="lazy"
                            alt=""
                            src="/star-11.svg"
                          />
                          <img
                            className={styles.starsChild}
                            loading="lazy"
                            alt=""
                            src="/star-21.svg"
                          />
                          <img
                            className={styles.starsChild}
                            loading="lazy"
                            alt=""
                            src="/star-31.svg"
                          />
                          <div className={styles.filledStarParent}>
                            <img
                              className={styles.filledStarIcon}
                              loading="lazy"
                              alt=""
                              src="/star-41.svg"
                            />
                            <img
                              className={styles.frameChild}
                              alt=""
                              src="/star-51.svg"
                            />
                          </div>
                        </div>
                        <div className={styles.priceWrapper}>
                          <div className={styles.price}>
                            <span>4.5/</span>
                            <span className={styles.span}>5</span>
                          </div>
                        </div>
                      </div>
                      <div className={styles.div}>98,000원</div>
                    </div>
                  </div>
                </div>
                <div className={styles.retroPatchHooded}>
                  Retro Patch Hooded Zip-Up 2024
                </div>
              </div>
              <div className={styles.frameWrapper4}>
                <div className={styles.frameParent6}>
                  <div className={styles.lineParent}>
                    <div className={styles.frameItem} />
                    <div className={styles.chooseSizeParent}>
                      <div className={styles.chooseSize}>Choose Size</div>
                      <div className={styles.frameParent7}>
                        <div className={styles.sWrapper}>
                          <div className={styles.s}>S</div>
                        </div>
                        <div className={styles.mWrapper}>
                          <div className={styles.m}>M</div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className={styles.frameItem} />
                  <div className={styles.chooseColorParent}>
                    <div className={styles.shop}>Choose Color</div>
                    <div className={styles.frameParent8}>
                      <button className={styles.wrapper}>
                        <div className={styles.div1}>화이트</div>
                      </button>
                      <button className={styles.container}>
                        <div className={styles.div1}>블랙</div>
                      </button>
                      <button className={styles.container}>
                        <div className={styles.div1}>차콜</div>
                      </button>
                      <button className={styles.frameButton}>
                        <div className={styles.div1}>베이비핑크</div>
                      </button>
                      <button className={styles.wrapper1}>
                        <div className={styles.div5}>핫핑크</div>
                      </button>
                    </div>
                  </div>
                  <div className={styles.frameItem} />
                  <div className={styles.addToCartParent}>
                    <div className={styles.addToCart}>
                      <img
                        className={styles.frameIcon2}
                        alt=""
                        src="/frame-81.svg"
                      />
                      <div className={styles.wrapper2}>
                        <div className={styles.shop}>1</div>
                      </div>
                      <img
                        className={styles.frameIcon2}
                        alt=""
                        src="/frame-9.svg"
                      />
                    </div>
                    <button className={styles.addCart}>
                      <div className={styles.addToCart1}>Add to Cart</div>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

FrameComponent2.propTypes = {
  className: PropTypes.string,
};

export default FrameComponent2;
