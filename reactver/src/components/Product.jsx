import FrameComponent3 from "./FrameComponent3";
import PropTypes from "prop-types";
import styles from "./Product.module.css";

const Product = ({ className = "" }) => {
  return (
    <div className={[styles.product, className].join(" ")}>
      <div className={styles.productDetails}>
        <div className={styles.productTitle}>
          <div className={styles.productName}>
            <div className={styles.current}>
              <img
                className={styles.productNameChild}
                loading="lazy"
                alt=""
                src="/frame-33@2x.png"
              />
              <div className={styles.list}>
                <div className={styles.logout}>
                  <div className={styles.checkeredShirtParent}>
                    <div className={styles.gradientGraphicTShirt}>
                      Gradient Graphic T-shirt
                    </div>
                    <div className={styles.productVariation}>
                      <div className={styles.sizeLarge}>
                        <span>{`Size: `}</span>
                        <span className={styles.large}>Large</span>
                      </div>
                      <div className={styles.colorWhite}>
                        <span>{`Color: `}</span>
                        <span className={styles.large}>White</span>
                      </div>
                    </div>
                  </div>
                  <div className={styles.div}>$145</div>
                </div>
                <FrameComponent3 />
              </div>
            </div>
            <div className={styles.productNameItem} />
          </div>
          <div className={styles.productName}>
            <div className={styles.current}>
              <img
                className={styles.productNameChild}
                alt=""
                src="/frame-33-1@2x.png"
              />
              <div className={styles.list}>
                <div className={styles.logout}>
                  <div className={styles.checkeredShirtParent}>
                    <div className={styles.gradientGraphicTShirt}>
                      C<span className={styles.heckered}>HECKERED</span> S
                      <span className={styles.heckered}>HIRT</span>
                    </div>
                    <div className={styles.productVariation}>
                      <div className={styles.sizeLarge}>
                        <span>{`Size: `}</span>
                        <span className={styles.large}>Medium</span>
                      </div>
                      <div className={styles.colorRed}>
                        <span>{`Color: `}</span>
                        <span className={styles.large}>Red</span>
                      </div>
                    </div>
                  </div>
                  <div className={styles.div}>$180</div>
                </div>
                <FrameComponent3 />
              </div>
            </div>
            <div className={styles.productNameItem} />
          </div>
          <div className={styles.productImage}>
            <div className={styles.imageContainer}>
              <img
                className={styles.image9Icon}
                loading="lazy"
                alt=""
                src="/image-9@2x.png"
              />
            </div>
            <div className={styles.list}>
              <div className={styles.logout}>
                <div className={styles.checkeredShirtParent}>
                  <div className={styles.gradientGraphicTShirt}>
                    S<span className={styles.heckered}>KINNY</span> F
                    <span className={styles.heckered}>IT</span> J
                    <span className={styles.heckered}>EANS</span>
                  </div>
                  <div className={styles.productVariation}>
                    <div className={styles.sizeLarge}>
                      <span>{`Size: `}</span>
                      <span className={styles.large}>Large</span>
                    </div>
                    <div className={styles.sizeLarge}>
                      <span>{`Color: `}</span>
                      <span className={styles.large}>Blue</span>
                    </div>
                  </div>
                </div>
                <div className={styles.div}>$240</div>
              </div>
              <FrameComponent3 />
            </div>
          </div>
        </div>
        <div className={styles.orderSummary}>
          <h3 className={styles.orderSummary1}>Order Summary</h3>
          <div className={styles.summaryDetails}>
            <div className={styles.summaryItems}>
              <div className={styles.gradientGraphicTShirt}>Subtotal</div>
              <div className={styles.summaryValues}>$565</div>
            </div>
            <div className={styles.summaryItems}>
              <div className={styles.gradientGraphicTShirt}>
                Discount (-20%)
              </div>
              <div className={styles.div2}>-$113</div>
            </div>
            <div className={styles.summaryItems}>
              <div className={styles.deliveryFee}>Delivery Fee</div>
              <div className={styles.summaryValues}>$15</div>
            </div>
            <div className={styles.summaryDetailsChild} />
            <div className={styles.summaryItems3}>
              <div className={styles.gradientGraphicTShirt}>Total</div>
              <div className={styles.div4}>$467</div>
            </div>
          </div>
          <div className={styles.promoCode}>
            <div className={styles.promoInput}>
              <img className={styles.frameIcon} alt="" src="/frame-15.svg" />
              <input
                className={styles.addPromoCode}
                placeholder="Add promo code"
                type="text"
              />
            </div>
            <button className={styles.applyButton}>
              <div className={styles.apply}>Apply</div>
            </button>
          </div>
          <button className={styles.checkout}>
            <div className={styles.goToCheckout}>Go to Checkout</div>
            <img
              className={styles.arrowDownBold1Icon}
              alt=""
              src="/arrowdownbold-1@2x.png"
            />
          </button>
        </div>
      </div>
    </div>
  );
};

Product.propTypes = {
  className: PropTypes.string,
};

export default Product;
