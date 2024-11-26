import OutfitPreview from "../components/OutfitPreview";
import Product from "../components/Product";
import Footer from "../components/Footer";
import styles from "./Cart.module.css";

const Cart = () => {
  return (
    <div className={styles.cart}>
      <section className={styles.outfitPreview}>
        <OutfitPreview />
        <div className={styles.navigation}>
          <div className={styles.navigation1}>
            <div className={styles.cart1}>
              <div className={styles.homeLink}>
                <a className={styles.home}>Home</a>
              </div>
              <div className={styles.wrapper}>
                <img className={styles.icon} alt="" src="/frame-6@2x.png" />
              </div>
              <div className={styles.cart2}>Cart</div>
            </div>
            <h1 className={styles.cart3}>Cart</h1>
          </div>
        </div>
        <Product />
      </section>
      <Footer
        footerMarginLeft="unset"
        hELPMENUTextDecoration="unset"
        badge="/badge2.svg"
        badge1="/badge-13.svg"
        badge2="/badge-23.svg"
        badge3="/badge-33.svg"
        badge4="/badge-43.svg"
      />
    </div>
  );
};

export default Cart;
